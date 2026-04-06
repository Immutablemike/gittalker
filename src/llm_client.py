"""
LLM Client Utility for GitTalker
Supports multiple LLM providers: OpenAI, Anthropic, Ollama, vLLM
"""

from typing import Any, Dict, List, Optional

import httpx

from src.config import (ENABLE_LLM_FALLBACK, FALLBACK_ORDER, LLM_CONFIGS,
                        MAX_TOKENS, PRIMARY_LLM_PROVIDER, REQUEST_TIMEOUT,
                        TEMPERATURE)


class LLMClient:
    """Universal LLM client supporting multiple providers"""

    def __init__(self):
        self.primary_provider = PRIMARY_LLM_PROVIDER
        self.configs = LLM_CONFIGS
        self.fallback_enabled = ENABLE_LLM_FALLBACK
        self.fallback_order = FALLBACK_ORDER

    async def generate_response(
        self, messages: List[Dict[str, str]], provider: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Generate response from LLM provider with fallback support

        Args:
            messages: List of message dicts with 'role' and 'content'
            provider: Optional specific provider to use

        Returns:
            Dict with response content and metadata
        """
        target_provider = provider or self.primary_provider

        # Try primary provider first
        try:
            return await self._call_provider(target_provider, messages)
        except Exception as e:
            print(f"Provider {target_provider} failed: {e}")

            # Try fallback providers if enabled
            if self.fallback_enabled and not provider:
                for fallback_provider in self.fallback_order:
                    if fallback_provider != target_provider:
                        try:
                            return await self._call_provider(
                                fallback_provider, messages
                            )
                        except Exception as fallback_e:
                            print(
                                f"Fallback {fallback_provider} failed: " f"{fallback_e}"
                            )
                            continue

            raise Exception("All LLM providers failed")

    async def _call_provider(
        self, provider: str, messages: List[Dict[str, str]]
    ) -> Dict[str, Any]:
        """Call specific LLM provider"""
        config = self.configs.get(provider)
        if not config or not config.get("enabled"):
            raise Exception(f"Provider {provider} not configured or disabled")

        if provider == "openai":
            return await self._call_openai(messages, config)
        elif provider == "anthropic":
            return await self._call_anthropic(messages, config)
        elif provider == "ollama":
            return await self._call_ollama(messages, config)
        elif provider == "vllm":
            return await self._call_vllm(messages, config)
        else:
            raise Exception(f"Unknown provider: {provider}")

    async def _call_openai(
        self, messages: List[Dict[str, str]], config: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Call OpenAI API"""
        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json",
        }

        if config.get("organization"):
            headers["OpenAI-Organization"] = config["organization"]

        payload = {
            "model": config["model"],
            "messages": messages,
            "temperature": TEMPERATURE,
            "max_tokens": MAX_TOKENS,
        }

        async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
            response = await client.post(
                f"{config['base_url']}/chat/completions", headers=headers, json=payload
            )
            response.raise_for_status()
            result = response.json()

            return {
                "content": result["choices"][0]["message"]["content"],
                "provider": "openai",
                "model": config["model"],
                "usage": result.get("usage", {}),
            }

    async def _call_anthropic(
        self, messages: List[Dict[str, str]], config: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Call Anthropic API"""
        headers = {
            "x-api-key": config["api_key"],
            "anthropic-version": config["version"],
            "Content-Type": "application/json",
        }

        # Convert messages format for Anthropic
        system_message = None
        anthropic_messages = []

        for msg in messages:
            if msg["role"] == "system":
                system_message = msg["content"]
            else:
                anthropic_messages.append(msg)

        payload = {
            "model": config["model"],
            "messages": anthropic_messages,
            "temperature": TEMPERATURE,
            "max_tokens": MAX_TOKENS,
        }

        if system_message:
            payload["system"] = system_message

        async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
            response = await client.post(
                f"{config['base_url']}/v1/messages", headers=headers, json=payload
            )
            response.raise_for_status()
            result = response.json()

            return {
                "content": result["content"][0]["text"],
                "provider": "anthropic",
                "model": config["model"],
                "usage": result.get("usage", {}),
            }

    async def _call_ollama(
        self, messages: List[Dict[str, str]], config: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Call Ollama API"""
        payload = {
            "model": config["model"],
            "messages": messages,
            "stream": False,
            "options": {"temperature": TEMPERATURE, "num_predict": MAX_TOKENS},
        }

        async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
            response = await client.post(f"{config['base_url']}/api/chat", json=payload)
            response.raise_for_status()
            result = response.json()

            return {
                "content": result["message"]["content"],
                "provider": "ollama",
                "model": config["model"],
                "usage": {
                    "eval_count": result.get("eval_count", 0),
                    "eval_duration": result.get("eval_duration", 0),
                },
            }

    async def _call_vllm(
        self, messages: List[Dict[str, str]], config: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Call vLLM API (OpenAI-compatible)"""
        headers = {"Content-Type": "application/json"}

        if config.get("api_key"):
            headers["Authorization"] = f"Bearer {config['api_key']}"

        payload = {
            "model": config["model"],
            "messages": messages,
            "temperature": TEMPERATURE,
            "max_tokens": MAX_TOKENS,
        }

        async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
            response = await client.post(
                f"{config['base_url']}/v1/chat/completions",
                headers=headers,
                json=payload,
            )
            response.raise_for_status()
            result = response.json()

            return {
                "content": result["choices"][0]["message"]["content"],
                "provider": "vllm",
                "model": config["model"],
                "usage": result.get("usage", {}),
            }

    def get_available_providers(self) -> List[str]:
        """Get list of available/configured providers"""
        return [
            provider
            for provider, config in self.configs.items()
            if config.get("enabled")
        ]

    def get_provider_info(self, provider: str) -> Dict[str, Any]:
        """Get configuration info for a specific provider"""
        config = self.configs.get(provider, {})
        return {
            "provider": provider,
            "enabled": config.get("enabled", False),
            "model": config.get("model", "unknown"),
            "base_url": config.get("base_url", "unknown"),
        }


# Example usage
async def example_usage():
    """Example of how to use the LLM client"""
    client = LLMClient()

    # Print available providers
    print("Available providers:", client.get_available_providers())

    # Example conversation
    messages = [
        {"role": "system", "content": "You are a helpful coding assistant."},
        {"role": "user", "content": "Explain Python async/await in simple terms."},
    ]

    try:
        # Use primary provider
        response = await client.generate_response(messages)
        print(f"Response from {response['provider']}: {response['content'][:100]}...")

        # Use specific provider
        response = await client.generate_response(messages, provider="ollama")
        print(f"Ollama response: {response['content'][:100]}...")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    import asyncio

    asyncio.run(example_usage())
