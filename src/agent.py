from openai import OpenAI
from typing import List, Dict, Tuple
import re
from .config import OPENAI_API_KEY, TEMPERATURE, AGENT_CONFIG


class GitTalkerAgent:
    def __init__(self):
        """Initialize GitTalker agent with enhanced personality."""
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.config = AGENT_CONFIG
        self.name = self.config["name"]
        
    async def generate_response(self, query: str, context: str) -> str:
        """Generate response with personality and scope enforcement."""
        # Check for out-of-scope queries
        if self._is_out_of_scope(query, context):
            return self._get_fallback_response("out_of_scope")
            
        # Check if we have relevant context
        if not context.strip():
            return self._get_fallback_response("no_docs_found")
            
        system_prompt = self._build_enhanced_system_prompt(context)
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",  # Using faster, better model
                temperature=TEMPERATURE,
                max_tokens=800,  # More generous token limit
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": self._enhance_user_query(query)}
                ]
            )
            
            return self._post_process_response(response.choices[0].message.content)
            
        except Exception as e:
            return self._get_fallback_response("technical_limits")
    
    def _build_enhanced_system_prompt(self, context: str) -> str:
        """Build comprehensive system prompt with personality and context."""
        base_prompt = self.config["system_prompt"]
        
        return f"""{base_prompt}

DOCUMENTATION CONTEXT FROM GITTALKER/ DIRECTORY:
{context}

Remember: Be enthusiastic and helpful while staying strictly within the repository documentation scope!"""
    
    def _is_out_of_scope(self, query: str, context: str) -> bool:
        """Check if query is outside our knowledge scope."""
        # If no relevant context found, it's likely out of scope
        if not context or len(context.strip()) < 50:
            return True
            
        # Keywords that suggest out-of-scope queries
        out_of_scope_indicators = [
            "personal", "weather", "news", "politics", "general programming",
            "unrelated", "off-topic", "what is", "who is", "when did",
            "wikipedia", "google", "search", "find me", "tell me about life"
        ]
        
        query_lower = query.lower()
        return any(indicator in query_lower for indicator in out_of_scope_indicators)
    
    def _get_fallback_response(self, fallback_type: str) -> str:
        """Get appropriate fallback response with urban flair."""
        fallbacks = self.config.get("fallbacks", {})
        base_response = fallbacks.get(fallback_type, 
            "Yo, you gotta ask Mike! I can only help with our project docs, no cap. 💭")
            
        # Urban greeting starters
        urban_starters = [
            "Yo! ", "Bet, ", "Say less! ", "Real talk, ", 
            "No cap, ", "Waddup fam! ", "Aight, "
        ]
        
        # Pick a starter based on fallback type
        if fallback_type == "out_of_scope":
            starter = "Yo! "
        elif fallback_type == "no_docs_found":
            starter = "Bet, "
        elif fallback_type == "uncertain":
            starter = "Real talk, "
        else:
            starter = "Aight, "
            
        return starter + base_response
    
    def _enhance_user_query(self, query: str) -> str:
        """Add context hints to user query with urban energy."""
        return f"""User question about our repo/build: {query}

Please respond with that urban energy while referencing specific docs when possible. Keep it 100! 💯"""
    
    def _post_process_response(self, response: str) -> str:
        """Post-process AI response to ensure urban consistency."""
        if not response:
            return self._get_fallback_response("technical_limits")
            
        # Ensure response doesn't accidentally go out of scope
        if "i don't know" in response.lower() or "i'm not sure" in response.lower():
            return self._get_fallback_response("uncertain")
            
        # Add encouraging closing if response seems complete but needs more energy
        if len(response) > 200 and not response.endswith(("?", "!", ".")):
            response += "\n\nNeed me to break that down more, fam? �"
            
        return response
    
    def is_valid_query(self, query: str) -> bool:
        """Enhanced validation for incoming queries."""
        if not query or len(query.strip()) < 3:
            return False
            
        # Check for malicious patterns
        dangerous_patterns = ["<script", "javascript:", "eval(", "exec("]
        query_lower = query.lower()
        
        if any(pattern in query_lower for pattern in dangerous_patterns):
            return False
            
        return True
    
    def get_personality_info(self) -> dict:
        """Get agent personality information for debugging/monitoring."""
        return {
            "name": self.name,
            "traits": self.config["personality"]["primary_traits"],
            "tone": self.config["personality"]["tone"],
            "specialization": self.config["personality"]["specialization"]
        }