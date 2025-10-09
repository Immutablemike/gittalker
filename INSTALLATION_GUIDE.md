# GitTalker 🤖💬

<div align="center">

**The client communication tool that eliminates daily standups and "what's the status?" interruptions.**

[![CI/CD](https://github.com/Immutablemike/gittalker/workflows/🔥%20CI/CD%20Pipeline/badge.svg)](https://github.com/Immutablemike/gittalker/actions)
[![Release](https://img.shields.io/github/v/release/Immutablemike/gittalker?style=flat-square)](https://github.com/Immutablemike/gittalker/releases)
![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Slack](https://img.shields.io/badge/Slack-4A154B?logo=slack&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?logo=openai&logoColor=white)

[Features](#features) • [Quick Start](#quick-start) • [Configuration](#configuration) • [Personalities](#agent-personalities) • [Usage Examples](#usage-examples) • [Contributing](#contributing)

</div>

---

## 🎯 **Problem → Solution**

GitTalker automatically updates your Slack channels with daily development progress, letting clients stay informed while developers stay focused. Query-friendly updates mean no more endless status meetings!

| **Before GitTalker** | **After GitTalker** |
|---------------------|-------------------|
| 🚫 Daily standup meetings | ✅ Automated daily progress updates |
| 🚫 "What's the status?" interruptions | ✅ Clients query project status anytime |
| 🚫 Context-switching to explain progress | ✅ Developers maintain focus on code |
| 🚫 Clients feeling out of the loop | ✅ Transparent communication within scope |
| 🚫 Time wasted on status meetings | ✅ More time building, less time explaining |

## ✨ **Features**

### 🤖 **Customizable Agent Personalities**
Choose from 5 pre-built personalities or create your own:
- **🎤 Jive Robot** - Urban energy, street-smart (original)
- **💼 Professional Consultant** - Corporate-friendly, polished  
- **🧠 Technical Expert** - Developer-focused, detailed
- **🤝 Friendly Guide** - Educational, supportive
- **⚡ Results-Driven** - Metrics-focused, action-oriented

**Customize everything:** Agent name, team branding, communication style, response patterns, and client interaction tone.

### 🔧 **Core Capabilities**
- **Slack Integration** - Real-time communication in your team channels
- **GitHub Repository Access** - Reads and understands your project documentation
- **Smart Scoping** - Only accesses designated directories (security-first)
- **RAG-Powered** - Uses retrieval-augmented generation for accurate responses
- **Daily Progress Updates** - Automated status reports for clients
- **Query-Friendly** - Clients can ask specific questions anytime

### 🛡️ **Built for Teams**
- **Multi-Client Support** - Different personalities for different clients
- **Brand Customization** - Your agent, your name, your style
- **Scope Control** - Define exactly what information is shared
- **Security-First** - Environment variables for all sensitive data
- **Production Ready** - Built with FastAPI, async/await, and proper error handling
- **Brand Customization** - Your agent, your name, your style
- **Scope Control** - Define exactly what information is shared
- **Security-First** - Environment variables for all sensitive data

---

## 🚀 **Quick Start**

### **Prerequisites**
- Python 3.8+
- Slack workspace (admin access to create apps)
- GitHub repository with documentation
- OpenAI API key

### **1. Clone & Install**
```bash
git clone https://github.com/Immutablemike/gittalker.git
cd gittalker
pip install -r requirements.txt
```

### **2. Set Up Slack App**

**Create a Slack App:**
1. Go to [api.slack.com/apps](https://api.slack.com/apps)
2. Click "Create New App" → "From scratch"
3. Name it "GitTalker" and select your workspace

**Configure OAuth Permissions:**
Add these Bot Token Scopes:
- `app_mentions:read`
- `channels:history` 
- `chat:write`
- `users:read`

**Enable Socket Mode:**
1. Go to "Socket Mode" in your app settings
2. Enable Socket Mode
3. Generate an App-Level Token with `connections:write` scope

**Install to Workspace:**
1. Go to "Install App"
2. Click "Install to Workspace"
3. Copy the Bot User OAuth Token

### **3. Set Up GitHub Access**

**Create GitHub Personal Access Token:**
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate new token with `repo` scope (for private repos) or `public_repo` (for public)
3. Copy the token

### **4. Configure Environment**

Create `.env` file:
```bash
cp .env.example .env
```

Edit `.env` with your credentials:
```bash
# Slack Configuration
SLACK_BOT_TOKEN=xoxb-your-slack-bot-token
SLACK_APP_TOKEN=xapp-your-app-level-token

# GitHub Configuration  
GITHUB_TOKEN=ghp_your-github-token
GITHUB_REPO_URL=https://github.com/yourusername/your-repo

# OpenAI Configuration
OPENAI_API_KEY=sk-your-openai-api-key

# Agent Personality (optional - defaults to jive robot)
AGENT_PROFILE=AGENT_Profiles/mike_jive_robot.json
```

### **5. Run GitTalker**
```bash
python src/main.py
```

**Test in Slack:**
- Invite your bot to a channel: `/invite @GitTalker`
- Ask a question: `@GitTalker what does this repository do?`
- Watch the magic happen! 🎉

---

## 🎭 **Agent Personalities**

GitTalker's secret sauce is customizable personalities. Check out `AGENT_Profiles/` for examples:

### **🎤 Jive Robot (Default)**
```json
{
  "agent_name": "GitTalker (Jive Robot)",
  "communication_style": "urban",
  "signature_phrases": ["No cap!", "That's fire!", "Let's get it!"]
}
```
**Perfect for:** Creative teams, startups, casual client relationships

### **💼 Professional Consultant**
```json
{
  "agent_name": "Development Assistant", 
  "communication_style": "professional",
  "signature_phrases": ["We remain committed to excellence"]
}
```
**Perfect for:** Enterprise clients, formal environments, C-suite communication

### **🧠 Technical Expert**
```json
{
  "agent_name": "Tech Lead Assistant",
  "communication_style": "technical", 
  "signature_phrases": ["From an implementation perspective"]
}
```
**Perfect for:** Developer-to-developer communication, technical stakeholders

### **Create Your Own**
1. Copy an existing profile from `AGENT_Profiles/`
2. Customize the personality traits and response patterns
3. Update your `.env` to use your custom profile
4. Restart GitTalker

**See [AGENT_Profiles/README.md](AGENT_Profiles/README.md) for complete customization guide.**

---

## ⚙️ **Configuration**

### **Environment Variables**

| Variable | Description | Required | Example |
|----------|-------------|----------|---------|
| `SLACK_BOT_TOKEN` | Bot User OAuth Token from Slack | ✅ | `xoxb-123...` |
| `SLACK_APP_TOKEN` | App-Level Token for Socket Mode | ✅ | `xapp-123...` |
| `GITHUB_TOKEN` | Personal Access Token | ✅ | `ghp_123...` |
| `GITHUB_REPO_URL` | Repository URL to access | ✅ | `https://github.com/user/repo` |
| `OPENAI_API_KEY` | OpenAI API key for GPT-4 | ✅ | `sk-123...` |
| `AGENT_PROFILE` | Path to personality profile | ❌ | `AGENT_Profiles/custom.json` |
| `REPO_SCOPE_PATH` | Limit access to specific directory | ❌ | `docs/` |

### **Repository Scope Control**

By default, GitTalker only accesses the `gittalker/` directory. To change this:

```bash
# Access entire repository
REPO_SCOPE_PATH=""

# Access only docs folder  
REPO_SCOPE_PATH="docs/"

# Access multiple folders (comma-separated)
REPO_SCOPE_PATH="docs/,src/,README.md"
```

### **Slack Channel Setup**

1. **Invite GitTalker:** `/invite @GitTalker` in your channel
2. **Set Channel Purpose:** Use for client updates and project Q&A
3. **Pin Important Info:** Pin setup instructions for team members
4. **Client Access:** Add clients to channel for transparency

---

## 🛠️ **Development**

### **Project Structure**
```
gittalker/
├── src/
│   ├── agent.py           # Core GitTalker agent logic
│   ├── config.py          # Configuration and personality system
│   ├── github_fetcher.py  # GitHub API integration
│   └── main.py            # Application entry point
├── AGENT_Profiles/        # Personality templates and customization
├── .github/               # Issue/PR templates and workflows
├── .env.example           # Environment template
└── requirements.txt       # Python dependencies
```

### **Running in Development**
```bash
# Install development dependencies
pip install -r requirements.txt

# Set up pre-commit hooks (optional)
pre-commit install

# Run with debug logging
export LOG_LEVEL=DEBUG
python src/main.py
```

### **Testing Different Personalities**
```bash
# Test professional personality
export AGENT_PROFILE=AGENT_Profiles/professional_consultant.json
python src/main.py

# Test technical personality  
export AGENT_PROFILE=AGENT_Profiles/technical_expert.json
python src/main.py
```

---

## 📚 **Usage Examples**

---

## 📚 **Usage Examples**

### **Repository Structure**

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

### **Personality Examples**

**In-Scope Query (Jive Robot):**
> **User:** "How do I install dependencies?"
> 
> **GitTalker:** "Yo, good question! 💯 Based on our setup docs, you just need to run `pip install -r requirements.txt` and you're straight. Need me to break that down more, fam?"

**In-Scope Query (Professional Consultant):**
> **User:** "How do I install dependencies?"
> 
> **GitTalker:** "I'd be happy to help you with the installation process. According to our project documentation, you'll need to run `pip install -r requirements.txt` to install all required dependencies. This will ensure your environment matches our development specifications."

**Out-of-Scope Query:**
> **User:** "What's the weather?"
> 
> **GitTalker:** "Yo! You gotta ask Mike! 💭 I only know what's in our project docs, no cap. That's outside my lane, fam."

### **Daily Progress Updates**
GitTalker automatically posts progress updates based on repository activity:

> **GitTalker (Jive Robot)**: Yo! Here's what's been happening with your project:
> 
> ✅ **Completed today**: Added user authentication system
> 🔄 **In progress**: Working on dashboard UI components  
> 📋 **Next up**: Database optimization and testing
> 
> No cap, we're making serious moves! 🔥

### **Client Q&A**
Clients can ask questions anytime:

> **Client**: @GitTalker what's the status of the mobile app feature?
> 
> **GitTalker**: Let me check the latest on mobile development... Based on the repository, we've completed the core mobile framework and are currently working on user interface components. The team's been on fire with the React Native integration! Next milestone is user testing by Friday. 💯

### **Technical Queries**
Perfect for developer-focused communication:

> **Stakeholder**: @GitTalker can you explain the architecture?
> 
> **GitTalker (Technical Expert)**: From an implementation perspective, the system uses a microservices architecture with FastAPI for the backend, React for the frontend, and PostgreSQL for data persistence. Here's the technical overview of each component...

---

## 🏗️ **Architecture**

- **FastAPI**: Modern async web framework for high-performance API
- **OpenAI GPT**: Language model for intelligent, contextual responses
- **Slack SDK**: Real-time chat integration with Socket Mode
- **RAG Engine**: Document retrieval and chunking for accurate responses
- **GitHub API**: Repository content fetching with scope control
- **Python 3.8+**: Modern Python with async/await support

## 🛡️ **Security Features**

- **Input Validation**: Prevents malicious queries and injection attacks
- **Scope Enforcement**: Bot only accesses designated directories
- **No Sensitive Data**: Responses never include credentials or private info
- **Environment Variables**: All sensitive configuration externalized
- **Automatic Escalation**: Complex queries escalated to human team members
- **Rate Limiting**: Built-in protection against API abuse

---

## 🌟 **Contributing**

We'd love your help making GitTalker even better! Here's how to get involved:

### **Quick Contribution Guide**
1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/awesome-feature`
3. **Make your changes** (keep that personality!)
4. **Test with your Slack workspace**
5. **Submit a pull request**

### **Types of Contributions We Need**
- 🎭 **New personality profiles** for different industries
- 🔧 **Integration improvements** (Discord, Teams, etc.)
- 📚 **Documentation enhancements**
- 🐛 **Bug fixes and performance improvements**
- 🌍 **Internationalization support**

### **Development Focus Areas**
- **Client Communication Patterns** - How do different industries communicate?
- **Personality Consistency** - Maintaining character across interactions
- **Security & Privacy** - Keeping client data safe
- **Scalability** - Supporting teams from solo devs to agencies

**See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.**

---

## 📋 **Roadmap**

### **🔥 Current Focus**
- [ ] Demo GIF and visual assets
- [ ] Integration documentation improvements
- [ ] Community engagement features

### **🚀 Next Phase**
- [ ] Discord integration
- [ ] Microsoft Teams support  
- [ ] Multi-repository support
- [ ] Analytics dashboard

### **💡 Future Ideas**
- [ ] Voice message support
- [ ] Custom webhook integrations
- [ ] AI-powered code review summaries
- [ ] Client portal web interface

---

## 🤝 **Community**

### **Get Help**
- 💬 **GitHub Discussions** - Questions and community chat
- 🐛 **Issues** - Bug reports and feature requests
- 🔒 **Private Contact** - [@Immutablemike](https://github.com/Immutablemike) for sensitive topics

### **Stay Updated**
- ⭐ **Star this repo** to stay notified of updates
- 👀 **Watch releases** for new personality profiles
- 🍴 **Fork and customize** for your team's needs

---

## 📄 **License**

MIT License - see [LICENSE](LICENSE) file for details.

---

## 🙏 **Acknowledgments**

- **OpenAI** for the GPT-4 API that powers intelligent responses
- **Slack** for the amazing platform and developer tools
- **GitHub** for hosting our code and community
- **Contributors** who help make GitTalker better every day
- Built with ❤️ for the developer community who inspired authentic AI interactions

---

<div align="center">

**Ready to eliminate those daily standups?** 

⭐ **Star this repo** • 🍴 **Fork for your team** • 💬 **Join the discussion**

**Made with 🔥 by developers, for developers. Keep it 100! 💯**

[@Immutablemike](https://github.com/Immutablemike) and the GitTalker community

</div>