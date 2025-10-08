from fastapi import FastAPI
from slack_sdk import WebClient
from slack_sdk.socket_mode import SocketModeClient
from slack_sdk.socket_mode.request import SocketModeRequest
from slack_sdk.socket_mode.response import SocketModeResponse
import asyncio
import uvicorn
from .config import SLACK_BOT_TOKEN, SLACK_APP_TOKEN
from .github_fetcher import GitHubDocsFetcher
from .rag_engine import SimpleRAG
from .agent import GitTalkerAgent

app = FastAPI(title="GitTalker", description="Slack bot for GitHub repository Q&A")

# Global instances
github_fetcher = GitHubDocsFetcher()
rag_engine = SimpleRAG()
gittalker_agent = GitTalkerAgent()
slack_client = WebClient(token=SLACK_BOT_TOKEN)


class SlackBot:
    def __init__(self):
        self.socket_client = SocketModeClient(
            app_token=SLACK_APP_TOKEN,
            web_client=slack_client
        )
        self.socket_client.socket_mode_request_listeners.append(
            self.handle_events
        )
        
    async def handle_events(self, client: SocketModeClient, req: SocketModeRequest):
        """Handle incoming Slack events."""
        if req.type == "events_api":
            event = req.payload["event"]
            
            # Handle app mentions
            if event["type"] == "app_mention":
                await self.handle_mention(event)
                
            # Handle direct messages
            elif event["type"] == "message" and "subtype" not in event:
                if event.get("channel_type") == "im":
                    await self.handle_dm(event)
        
        # Acknowledge the event
        response = SocketModeResponse(envelope_id=req.envelope_id)
        client.send_socket_mode_response(response)
    
    async def handle_mention(self, event):
        """Handle @bot mentions in channels."""
        channel = event["channel"]
        user = event["user"]
        text = event["text"]
        
        # Remove bot mention from text
        clean_text = self.clean_mention_text(text)
        
        if gittalker_agent.is_valid_query(clean_text):
            response = await self.process_query(clean_text)
            
            slack_client.chat_postMessage(
                channel=channel,
                text=response,
                thread_ts=event.get("ts")  # Reply in thread if possible
            )
    
    async def handle_dm(self, event):
        """Handle direct messages to the bot."""
        channel = event["channel"]
        user = event["user"]
        text = event["text"]
        
        if gittalker_agent.is_valid_query(text):
            response = await self.process_query(text)
            
            slack_client.chat_postMessage(
                channel=channel,
                text=response
            )
    
    async def process_query(self, query: str) -> str:
        """Process user query and generate response."""
        try:
            # Search documentation
            search_results = rag_engine.search(query, top_k=3)
            context = rag_engine.format_context(search_results)
            
            # Generate response
            response = await gittalker_agent.generate_response(query, context)
            
            return response
            
        except Exception as e:
            return f"Sorry, I encountered an error processing your question: {str(e)}"
    
    def clean_mention_text(self, text: str) -> str:
        """Remove bot mention from message text."""
        import re
        # Remove <@USER_ID> mentions
        clean_text = re.sub(r'<@[A-Z0-9]+>', '', text).strip()
        return clean_text
    
    def start(self):
        """Start the Slack bot."""
        self.socket_client.connect()


# Initialize bot
slack_bot = SlackBot()


@app.on_event("startup")
async def startup_event():
    """Initialize documentation on startup."""
    try:
        print("Fetching documentation from GitHub...")
        docs = await github_fetcher.fetch_docs()
        
        print(f"Indexing {len(docs)} documents...")
        rag_engine.index_documents(docs)
        
        print("Starting Slack bot...")
        slack_bot.start()
        
        print("DocsBot is ready!")
        
    except Exception as e:
        print(f"Startup error: {e}")


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "DocsBot"}


if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )