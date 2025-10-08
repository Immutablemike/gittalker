# GitTalker - Intelligent GitHub Repository Assistant

A enthusiastic and helpful Slack bot that reads documentation from your GitHub repository's `gittalker/` directory and answers client questions with personality! 🚀

## ✨ Key Features

- **Personality-Driven**: Warm, enthusiastic, and professional responses
- **Scope-Protected**: Only answers questions about your repository documentation
- **Smart Fallbacks**: "You gotta ask Mike!" for out-of-scope queries
- **Security-First**: Input validation and guardrails built-in
- **Controlled Content**: Only accesses files in the `gittalker/` directory

## Quick Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
Copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

### 3. Get Your API Keys

**OpenAI API Key:**
- Visit: https://platform.openai.com/api-keys
- Create new secret key

**GitHub Personal Access Token:**
- Visit: https://github.com/settings/tokens
- Generate new token with `repo` scope (for private repos) or no scopes (for public repos)

**Slack Bot Setup:**
1. Go to https://api.slack.com/apps
2. Create New App → "From scratch"
3. App Name: "DocsBot", choose your workspace
4. **OAuth & Permissions** → Bot Token Scopes:
   - `app_mentions:read`
   - `chat:write`
   - `im:read`
   - `im:write`
5. **Install App** → Install to Workspace
6. Copy **Bot User OAuth Token** (starts with `xoxb-`)
7. **Socket Mode** → Enable Socket Mode
8. Generate **App-Level Token** with `connections:write` scope
9. **Event Subscriptions** → Enable Events → Subscribe to:
   - `app_mention`
   - `message.im`

### 4. Run the Bot
```bash
python -m uvicorn src.main:app --reload
```

## Usage

- **@DocsBot** mention in channels
- **Direct message** the bot
- Ask questions about your repository documentation

## Configuration

Edit `src/config.py` to customize:
- Agent personality
- System prompts
- Response guardrails
- Model parameters

## Architecture

- **FastAPI** - Web framework
- **Slack SDK** - Real-time Slack integration
- **OpenAI** - LLM for responses
- **sentence-transformers** - Document embeddings
- **httpx** - GitHub API client

## Files

- `src/main.py` - FastAPI app + Slack bot
- `src/github_fetcher.py` - GitHub docs fetcher
- `src/rag_engine.py` - RAG search engine
- `src/agent.py` - OpenAI integration
- `src/config.py` - Configuration and prompts

Simple, production-ready, and follows DRY/KISS/YAGNI principles.