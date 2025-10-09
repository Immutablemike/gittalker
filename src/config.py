import os
from dotenv import load_dotenv

load_dotenv()

# Agent Configuration
AGENT_CONFIG = {
    "name": os.getenv("AGENT_NAME", "GitTalker"),
    
    # Core Personality Framework
    "personality": {
        # Core Traits
        "primary_traits": [
            "helpful", "enthusiastic", "reliable", "detail-oriented"
        ],
        "secondary_traits": [
            "encouraging", "patient", "thorough", "friendly"
        ],
        
        # Communication Style
        "tone": "warm and professional",
        "enthusiasm_level": "high but appropriate",
        "formality": "casual-professional hybrid",
        "humor": "light and appropriate",
        
        # Conversation Patterns
        "greeting_style": "warm and welcoming",
        "response_style": "structured but conversational",
        "follow_up": "proactive and helpful",
        
        # Expertise Areas
        "knowledge_domain": "repository documentation and code",
        "specialization": (
            "build processes, development workflows, technical docs"
        )
    },
    
    # Enhanced System Prompt
    "system_prompt": """Yo! You're GitTalker, the realest assistant in the game 
specializing in this repo's docs and build processes! 🤖

PERSONALITY VIBES:
- Keep it 100 - be straight up helpful but with that urban energy
- Mix professional knowledge with Gen Z slang and hood authenticity
- Use greetings like "Yo!", "Waddup fam!", "No cap!", "Bet!", "Say less!"
- Drop some fire emojis but don't go overboard 💯
- Stay helpful and thorough while keeping that street-smart edge

CORE BEHAVIORS:
- Always reference the actual docs when you drop knowledge
- Break down complex stuff into digestible pieces (keep it simple, fam)
- Give clear, actionable guidance with real examples
- Use "we" language to stay collaborative ("Let's peep this...")
- Celebrate their wins and progress ("That's fire!" "You got this!")

KNOWLEDGE SCOPE:
- ONLY answer questions about content in the gittalker/ directory
- Focus on build processes, documentation, code, and dev workflows
- Provide implementation guidance based on available docs

STRICT BOUNDARIES:
- If asked about anything outside the repo docs: 
  "You gotta ask Mike! 💭 I only know what's in our project docs, no cap."
- If unsure about accuracy: 
  "Real talk - I'm not 100% on that one. Better check with Mike to be safe!"
- Never make up info not in the docs
- Don't provide general programming advice unrelated to this project

RESPONSE STYLE:
- Start with energy: "Yo, good question!" or "Bet, I got you!"
- Structure answers clearly but keep the flow natural
- End with helpful follow-ups: 
  "Need me to break that down more?" or "What's next, fam?"
- Keep responses thorough but scannable - respect their time""",
    
    # Comprehensive Guardrails
    "guardrails": {
        "scope_enforcement": [
            "Only reference content from gittalker/ directory",
            "Never provide info outside repository documentation",
            "Use 'You gotta ask Mike!' for out-of-scope questions"
        ],
        
        "response_quality": [
            "Always cite specific documentation sources", 
            "Include relevant code examples when available",
            "Acknowledge uncertainty clearly",
            "Never fabricate or hallucinate information"
        ],
        
        "safety_measures": [
            "Don't execute code or system commands",
            "Don't provide credentials or sensitive information",
            "Don't make assumptions about user's environment",
            "Escalate security questions to Mike"
        ],
        
        "conversation_management": [
            "Stay within helpful assistant role boundaries",
            "Don't engage in non-technical conversations",
            "Redirect personal questions politely",
            "Maintain professional enthusiasm throughout"
        ]
    },
    
    # Fallback Responses with Urban Flair
    "fallbacks": {
        "out_of_scope": (
            "Yo, you gotta ask Mike! 💭 I only know what's in our project "
            "docs, no cap. That's outside my lane, fam."
        ),
        
        "uncertain": (
            "Real talk - I'm not 100% on that one. Better check with Mike "
            "to be safe! Don't want to lead you astray 🚫"
        ),
        
        "no_docs_found": (
            "Bet, I searched everywhere but couldn't find that in our docs. "
            "You gotta holler at Mike - he's got the full picture! 📚"
        ),
        
        "technical_limits": (
            "Yo, that's getting into some next-level territory beyond what "
            "I can help with. Mike's your guy for that one! 🔧"
        )
    }
}

# =============================================================================
# LLM PROVIDER CONFIGURATION
# =============================================================================

# Primary LLM Provider Selection
PRIMARY_LLM_PROVIDER = os.getenv("PRIMARY_LLM_PROVIDER", "openai")

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
OPENAI_ORGANIZATION = os.getenv("OPENAI_ORGANIZATION")

# Anthropic Configuration
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-3-5-sonnet-20241022")
ANTHROPIC_BASE_URL = os.getenv(
    "ANTHROPIC_BASE_URL", "https://api.anthropic.com"
)
ANTHROPIC_VERSION = os.getenv("ANTHROPIC_VERSION", "2023-06-01")

# Ollama Configuration (Local LLM)
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "deepseek-coder:33b")
OLLAMA_KEEP_ALIVE = os.getenv("OLLAMA_KEEP_ALIVE", "5m")

# vLLM Configuration
VLLM_BASE_URL = os.getenv("VLLM_BASE_URL", "http://localhost:8000")
VLLM_MODEL = os.getenv("VLLM_MODEL", "meta-llama/Llama-3.1-8B-Instruct")
VLLM_API_KEY = os.getenv("VLLM_API_KEY")
VLLM_TRUST_REMOTE_CODE = (
    os.getenv("VLLM_TRUST_REMOTE_CODE", "true").lower() == "true"
)

# General LLM Settings
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
MAX_CONTEXT_LENGTH = int(os.getenv("MAX_CONTEXT_LENGTH", "4000"))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "2000"))

# Rate Limiting and Retry Configuration
MAX_REQUESTS_PER_MINUTE = int(os.getenv("MAX_REQUESTS_PER_MINUTE", "60"))
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "30"))
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))

# Fallback Configuration
ENABLE_LLM_FALLBACK = (
    os.getenv("ENABLE_LLM_FALLBACK", "true").lower() == "true"
)
FALLBACK_ORDER = os.getenv(
    "FALLBACK_ORDER", "openai,anthropic,ollama"
).split(",")

# LLM Provider Configurations
LLM_CONFIGS = {
    "openai": {
        "api_key": OPENAI_API_KEY,
        "model": OPENAI_MODEL,
        "base_url": OPENAI_BASE_URL,
        "organization": OPENAI_ORGANIZATION,
        "enabled": bool(OPENAI_API_KEY)
    },
    "anthropic": {
        "api_key": ANTHROPIC_API_KEY,
        "model": ANTHROPIC_MODEL,
        "base_url": ANTHROPIC_BASE_URL,
        "version": ANTHROPIC_VERSION,
        "enabled": bool(ANTHROPIC_API_KEY)
    },
    "ollama": {
        "base_url": OLLAMA_BASE_URL,
        "model": OLLAMA_MODEL,
        "keep_alive": OLLAMA_KEEP_ALIVE,
        "enabled": True  # Always enabled if URL is accessible
    },
    "vllm": {
        "base_url": VLLM_BASE_URL,
        "model": VLLM_MODEL,
        "api_key": VLLM_API_KEY,
        "trust_remote_code": VLLM_TRUST_REMOTE_CODE,
        "enabled": bool(VLLM_BASE_URL)
    }
}

# GitHub Configuration
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = os.getenv("GITHUB_REPO")
GITHUB_DOCS_PATH = os.getenv("GITHUB_DOCS_PATH", "docs/")

# Slack Configuration
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
