from openai import OpenAI
from typing import List, Dict
import re
import html
import logging
from .config import OPENAI_API_KEY, TEMPERATURE, AGENT_CONFIG

logger = logging.getLogger(__name__)


class GitTalkerAgent:
    def __init__(self):
        """Initialize GitTalker agent with enhanced security."""
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.config = AGENT_CONFIG
        self.name = self.config["name"]
        self.query_count = {}  # Simple rate limiting
        
    def _sanitize_input(self, text: str) -> str:
        """Sanitize user input to prevent injection attacks."""
        if not text or not isinstance(text, str):
            return ""
            
        # Remove potentially dangerous characters
        text = html.escape(text)
        
        # Remove script tags and javascript
        text = re.sub(r'<script.*?</script>', '', text, flags=re.IGNORECASE)
        text = re.sub(r'javascript:', '', text, flags=re.IGNORECASE)
        text = re.sub(r'eval\s*\(', '', text, flags=re.IGNORECASE)
        text = re.sub(r'exec\s*\(', '', text, flags=re.IGNORECASE)
        
        # Limit length to prevent DoS
        if len(text) > 2000:
            text = text[:2000]
            
        return text.strip()
        
    def _check_rate_limit(self, user_id: str = "default") -> bool:
        """Simple rate limiting - max 10 queries per minute."""
        import time
        current_time = time.time()
        
        if user_id not in self.query_count:
            self.query_count[user_id] = []
            
        # Remove queries older than 1 minute
        self.query_count[user_id] = [
            t for t in self.query_count[user_id]
            if current_time - t < 60
        ]
        
        # Check if under limit
        if len(self.query_count[user_id]) >= 10:
            return False
            
        # Add current query
        self.query_count[user_id].append(current_time)
        return True
        
    async def generate_response(self, query: str, context: str) -> str:
        """Generate response with security and scope enforcement."""
        # Sanitize input
        query = self._sanitize_input(query)
        context = self._sanitize_input(context)
        
        # Rate limiting check
        if not self._check_rate_limit():
            return (
                "Whoa there! You're asking questions faster than I can think! "
                "Take a breather and try again in a minute. 🔥"
            )
        
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
                timeout=30,  # 30 second timeout
                messages=[
                    {"role": "system", "content": system_prompt},
                    {
                        "role": "user",
                        "content": self._enhance_user_query(query)
                    }
                ]
            )
            
            return self._post_process_response(
                response.choices[0].message.content
            )
            
        except Exception:
            logger.error("OpenAI API error occurred")
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
        base_response = fallbacks.get(
            fallback_type,
            "Yo, you gotta ask Mike! I can only help with our project docs, "
            "no cap. 💭"
        )
            
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

Please respond with that urban energy while referencing specific docs
when possible. Keep it 100! 💯"""
    
    def _post_process_response(self, response: str) -> str:
        """Post-process AI response to ensure urban consistency."""
        if not response:
            return self._get_fallback_response("technical_limits")
            
        # Ensure response doesn't accidentally go out of scope
        uncertain_phrases = ["i don't know", "i'm not sure"]
        if any(phrase in response.lower() for phrase in uncertain_phrases):
            return self._get_fallback_response("uncertain")
            
        # Add encouraging closing if response seems complete but needs energy
        if len(response) > 200 and not response.endswith(("?", "!", ".")):
            response += "\n\nNeed me to break that down more, fam? 💪"
            
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
