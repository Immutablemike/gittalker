# GitTalker 🔥

> **Yo! The realest GitHub repository assistant with that urban energy** 💯

GitTalker is an intelligent Slack bot that reads documentation from your GitHub repository and answers questions with personality! Built with modern AI, it keeps responses scoped to your repository content while bringing that authentic street-smart energy to client interactions.

## ✨ Features

- **🎭 Urban Personality**: Warm, authentic responses with Gen Z energy and professional knowledge
- **🎯 Scope Protection**: Only answers questions about your repository documentation  
- **🛡️ Smart Guardrails**: Input validation and automatic fallbacks to human escalation
- **📁 Controlled Access**: Only reads from designated `gittalker/` directory
- **🔄 RAG-Powered**: Uses retrieval-augmented generation for accurate, contextual responses
- **⚡ Production Ready**: Built with FastAPI, async/await, and proper error handling

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- OpenAI API key
- GitHub Personal Access Token
- Slack Bot setup

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/gittalker.git
cd gittalker
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment**
```bash
cp .env.example .env
# Edit .env with your API keys
```

4. **Run the bot**
```bash
python -m uvicorn src.main:app --reload
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with these variables:

```bash
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here
TEMPERATURE=0.7

# GitHub Configuration  
GITHUB_TOKEN=your_github_personal_access_token_here
GITHUB_REPO=your_username/your_repo_name

# Slack Configuration
SLACK_BOT_TOKEN=xoxb-your-bot-token-here
SLACK_APP_TOKEN=xapp-your-app-token-here

# Agent Configuration
AGENT_NAME=GitTalker
```

### GitHub Setup

1. Create a Personal Access Token at [github.com/settings/tokens](https://github.com/settings/tokens)
2. For public repos: No scopes needed
3. For private repos: Select `repo` scope

### Slack Bot Setup

1. Go to [api.slack.com/apps](https://api.slack.com/apps)
2. Create New App → "From scratch"
3. Configure these scopes:
   - `app_mentions:read`
   - `chat:write`
   - `im:read`
   - `im:write`
4. Enable Socket Mode
5. Subscribe to events: `app_mention`, `message.im`

## 📚 Usage

### Repository Structure

Create a `gittalker/` directory in your repository with documentation you want the bot to access:

```
your-repo/
├── gittalker/           # Bot can only read from here
│   ├── setup.md
│   ├── api-docs.md
│   └── troubleshooting.md
├── src/                 # Bot cannot access
├── private-configs/     # Bot cannot access
└── README.md           # Bot cannot access
```

### Personality Examples

**In-Scope Query:**
> **User:** "How do I install dependencies?"
> 
> **GitTalker:** "Yo, good question! 💯 Based on our setup docs, you just need to run `pip install -r requirements.txt` and you're straight. Need me to break that down more, fam?"

**Out-of-Scope Query:**
> **User:** "What's the weather?"
> 
> **GitTalker:** "Yo! You gotta ask Mike! 💭 I only know what's in our project docs, no cap. That's outside my lane, fam."

## 🏗️ Architecture

- **FastAPI**: Modern async web framework
- **OpenAI GPT**: Language model for responses
- **Slack SDK**: Real-time chat integration
- **RAG Engine**: Document retrieval and chunking
- **GitHub API**: Repository content fetching

## 🛡️ Security

- Input validation prevents malicious queries
- Scope enforcement limits bot knowledge
- No sensitive data in responses
- Environment variable configuration
- Automatic human escalation for complex queries

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with ❤️ for the developer community
- Inspired by the need for more authentic AI interactions
- Special thanks to the open source community

## 🔗 Links

- [Documentation](docs/)
- [Issues](https://github.com/yourusername/gittalker/issues)
- [Discussions](https://github.com/yourusername/gittalker/discussions)

---

**Made with 🔥 by developers, for developers. Keep it 100! 💯**