# GitTalker 🤖�

**The client communication tool that eliminates daily standups and "what's the status?" interruptions.**

GitTalker automatically updates your Slack channels with daily development progress, letting clients stay informed while developers stay focused. Query-friendly updates mean no more endless status meetings!

## 🎯 **Problem Solved**

**Before GitTalker:**
- Daily standup meetings interrupting flow state
- Constant "what's the status?" Slack messages  
- Developers context-switching to explain progress
- Clients feeling out of the loop
- Time wasted on status updates instead of building

**After GitTalker:**
- Automated daily progress updates to Slack
- Clients can query project status anytime
- Developers maintain focus on code
- Transparent communication within project scope
- More time building, less time explaining

## 🤖 **Customizable Agent Personalities**

GitTalker adapts to your team's communication style with the `AGENT_Profiles/` system:

- **🎤 Jive Robot** (Urban energy, street-smart, Mike's original)
- **💼 Professional Consultant** (Corporate-friendly, polished)
- **🧠 Technical Expert** (Developer-focused, detailed)
- **🤝 Friendly Guide** (Educational, supportive)
- **⚡ Results-Driven** (Metrics-focused, action-oriented)

**Customize everything:** Agent name, team branding, communication style, response patterns, and client interaction tone.

**🌟 This is now an Open Source project!** Check out the public repo at [github.com/Immutablemike/gittalker](https://github.com/Immutablemike/gittalker) for the community version.

## 📋 Project Status & Development Journey

This project evolved from a private client tool into a full open-source project with dual-repo strategy:

### 🔒 **Private Development** (This Repo)
- **Purpose**: Personal production version with credentials and private configs
- **URL**: `https://github.com/Immutablemike/gittalker-private`
- **Branch**: `main` - Contains your working environment with API keys
- **Use Case**: Your personal GitTalker instance for client work

### 🌍 **Public OSS** (Community Repo)  
- **Purpose**: Open source version for the developer community
- **URL**: `https://github.com/Immutablemike/gittalker`
- **Branch**: `main` (synced from `public-oss` branch here)
- **Use Case**: Community contributions, forks, and public installations

### 🔄 **Sync Strategy**
- Features developed in private can be cherry-picked to public (sanitized)
- Community contributions from public can be merged back to private
- Separate `.env` handling prevents credential leaks
- Clean separation of concerns

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

## 🔄 Development Workflow (Private Repo)

Since this is the private development version, here's how to work with both repos:

### **Working on Private Features**
```bash
# Stay on main branch for private work
git checkout main
git add .
git commit -m "Add private feature"
git push origin main
```

### **Preparing Features for OSS**
```bash
# Switch to public branch for OSS contributions
git checkout public-oss
git cherry-pick <commit-hash>  # Pick specific commits
# OR merge specific features
git merge main --no-ff
# Remove any sensitive data, then:
git push public public-oss:main
```

### **Syncing Community Contributions**
```bash
# Pull public repo changes
git fetch public
git checkout main
git cherry-pick <public-commit-hash>
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

**Public OSS Version:**
- [Main Repository](https://github.com/Immutablemike/gittalker) 🌍
- [Issues & Feature Requests](https://github.com/Immutablemike/gittalker/issues)
- [Community Discussions](https://github.com/Immutablemike/gittalker/discussions)

**Private Development:**
- [Private Repository](https://github.com/Immutablemike/gittalker-private) 🔒
- This repo for personal/client work

## 🚀 OSS Journey Notes

This project started as a private client tool and evolved into an open source project! The dual-repo strategy allows for:

- **Clean community engagement** without exposing sensitive configs
- **Private development** for client work and experiments  
- **Feature sharing** between private and public versions
- **Professional OSS presence** with proper documentation and licensing

The urban personality was born from wanting AI assistants that feel more authentic and relatable while maintaining professional utility. No cap, this approach brings some humanity back to AI interactions! 💯

---

**Made with 🔥 by developers, for developers. Keep it 100! 💯**