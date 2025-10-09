# GitTalker - AI-Powered Project Communication

**Embed an AI agent in your repository that provides real-time project updates and Q&A management to stakeholders in Slack - eliminate daily standups with automated, timestamped progress communication**

## 🎯 The Problem

**Modern development teams waste countless hours on status updates:**
- Daily standups that interrupt deep work
- "What's the status?" Slack messages every few hours  
- Non-technical stakeholders needing constant project visibility
- Founders and senior devs requiring progress transparency
- Repetitive explanations of the same project details

**The cost:** Broken focus, context-switching, and projects that take 2x longer due to communication overhead.

## ⚡ The Solution

GitTalker embeds an AI agent in your repository that becomes your **automated project communication system**. Stakeholders get instant, accurate project updates without interrupting your development flow.

**Replace daily standups with real-time project intelligence:**
- **Automated progress updates** triggered by commits and milestones
- **Timestamped project status** available 24/7 in Slack
- **Stakeholder self-service** for project questions and timeline queries
- **Professional communication** even when you're heads-down coding

**One-line installation:**
```bash
curl -fsSL https://raw.githubusercontent.com/Immutablemike/gittalker/main/INSTALL/install.sh | bash
```

## � How It Works

**Automated Stakeholder Communication:**

### Professional Project Updates
- **Mirror key documentation** → Copy README, roadmap, or changelog to your knowledge base
- **Automated progress tracking** → Timestamp updates triggered by commits and milestones  
- **Self-service project information** → Stakeholders get instant answers without interrupting dev work
- **Customizable communication style** → Choose from professional, technical, or friendly AI personalities

### Intelligent Scope Management
Stakeholders can ask project questions and get informed responses:

```text
Stakeholder: "What's included in this project?"
GitTalker: Based on the project scope, we're building:
• User authentication system
• Dashboard with analytics 
• Mobile-responsive design
• Basic reporting features

NOT included: Advanced reporting, third-party integrations, mobile app.

Stakeholder: "Can we add real-time notifications?"
GitTalker: That's outside my current knowledge scope - ask Mike directly for scope changes and timeline impact.
```

### Developer-Focused Benefits
For developers who need to maintain focus while keeping stakeholders informed:

- **Controlled information sharing** → You decide what goes in the knowledge base
- **Professional communication** → Consistent, polished responses even when you're busy
- **Scope boundary enforcement** → Clear "in scope" vs "ask developer directly" responses
- **Context preservation** → No more explaining the same project details repeatedly

## 🚀 What Gets Installed

**Full GitTalker AI Agent Service** - Not just a client, but the complete AI agent that embeds in your project:

```bash
your-project/
├── .gittalker/                    # GitTalker AI agent directory
│   ├── src/                       # Complete AI agent source code
│   ├── gittalker/                 # Your controlled knowledge base
│   │   ├── project-overview.md    # Mirror of your README
│   │   ├── progress-log.md        # Daily timestamped updates
│   │   ├── faq.md                 # Client questions & answers
│   │   └── roadmap.md             # Timeline & scope boundaries
│   ├── AGENT_Profiles/            # Personality options
│   ├── .env.example               # API keys & Slack setup
│   ├── requirements.txt           # Python dependencies
│   └── start-gittalker.sh         # Launch your AI agent
```

**Project Detection:**
- **Python** (FastAPI, Django, Flask)
- **JavaScript/TypeScript** (React, Node.js, Next.js)  
- **Go** (Standard projects with go.mod)
- **Rust** (Cargo projects)
- **Java** (Maven, Gradle)
- **PHP** (Composer projects)
- **Any project** (Generic documentation support)

## 🎭 Agent Personalities

Choose how your AI communicates with stakeholders:

- **🎤 Jive Robot** - Urban energy, authentic (default)
- **💼 Professional Consultant** - Corporate-friendly, polished
- **🧠 Technical Expert** - Developer-focused, detailed
- **🤝 Friendly Guide** - Educational, supportive  
- **⚡ Results-Driven** - Metrics-focused, action-oriented

## 🔌 Multi-Platform Client Management

**Beyond Slack** - GitTalker integrates with your existing client communication stack:

### Current Integrations
- **🟢 Slack** - Full featured (default)
- **🔵 Discord** - Community/gaming teams  
- **🟠 Microsoft Teams** - Enterprise environments

### Planned Integrations (Q1 2025)
- **📋 Linear** - Issue tracking + stakeholder updates
- **📝 Notion** - Documentation + project wikis
- **🎯 Monday.com** - Project management + client portals

### Meeting Intelligence Vision 🎯
**The Future of Developer-Client Meetings** - Imagine having full AI-enhanced knowledge of your codebase at your fingertips during client calls. While platforms like Cluely (enterprise meeting intelligence) don't currently offer public APIs, the vision is clear: GitTalker's project context + real-time meeting AI = next-level developer superpower.

**What this would enable:**
- 📊 **Real-time project context** during client presentations
- 🔍 **Instant code explanations** for non-technical stakeholders  
- ⚡ **Timeline & progress data** accessible during meetings
- 🎯 **Smart follow-up generation** based on project status

*Note: Currently exploring integration pathways with meeting intelligence platforms as they open developer access.*

## ⚙️ Quick Setup

```bash
cd .gittalker
./gittalker config      # Add API keys & Slack bot
./gittalker knowledge   # Customize project docs
./gittalker start       # Launch AI agent
```

**What you need:**
- **LLM API Key** (OpenAI, Anthropic, Ollama, or vLLM)
- **Slack Bot Token** (for client communication)
- **5 minutes** to customize your knowledge base

## 💬 Real Stakeholder Interactions

**Professional Progress Updates:**

```text
Stakeholder: "What's the current status?"
GitTalker: Here's today's progress update:

✅ Completed: User login system, password reset
🔄 In Progress: Dashboard UI components (75% complete)
📋 Next: User profile management, testing phase
🎯 On track for Friday milestone

Last updated: Oct 9, 2025 2:30 PM
```

**Automated Commit-Based Updates:**

```text
GitTalker: 🚀 Development Update (triggered by latest commit):

Just completed: Authentication module with OAuth integration
Files updated: auth.py, login.html, user-controller.js
Next milestone: Dashboard components (estimated 2 days)

Commit: "Add OAuth authentication flow" - 2 hours ago
```

### Custom Configuration

Edit `.gittalker/config.json` to customize file scanning:

```json
{
    "scan_patterns": {
        "python": ["**/*.py", "**/requirements.txt", "**/docs/**"]
    },
    "ai_focus_areas": ["code_quality", "performance", "testing"]
}
```

### Command Options

```bash
./gittalker chat    # Interactive chat mode
./gittalker scan    # Rescan project files  
./gittalker docs    # Generate documentation

# Shorthand versions
./gittalker c       # Chat
./gittalker s       # Scan
./gittalker d       # Docs
```

### Python API

Use GitTalker programmatically:

## 🔧 Customizing Your Knowledge Base

**Mirror important project docs:**
```bash
# Copy key project information
cp README.md .gittalker/gittalker/project-overview.md
cp CHANGELOG.md .gittalker/gittalker/progress-log.md

# Create controlled updates
echo "$(date): Authentication module completed" >> .gittalker/gittalker/daily-updates.md
```

**Scope boundary examples:**
```markdown
# What's NOT included in this project:
- Real-time chat features
- Third-party payment processing  
- Mobile app (web-responsive only)
- Advanced analytics dashboard

# Questions outside scope:
Ask Mike directly for timeline changes, budget discussions, or scope modifications.
```

## 🛡️ Why This Matters

**For Solo Developers:**
- Clients get instant answers without interrupting your flow
- Professional communication even when you're heads-down coding
- Clear project boundaries prevent scope creep conversations

**For Development Teams:**  
- Consistent project communication across all team members
- Junior devs protected from client pressure and scope discussions
- Senior devs freed from constant status update requests

**For Agencies:**
- Scale client communication without hiring more account managers
- Maintain professional client relationships with less overhead
- Protect billable development time from communication tasks

## �️ For Developers: Focus Protection

**The developer-focused benefits** that protect your deep work:

**Controlled Information Sharing:**
- **You curate the knowledge base** - Only information you put in `gittalker/` gets shared
- **Scope boundary enforcement** - Requests outside your documentation get redirected to you
- **Professional communication** - Consistent, polished responses even when you're heads-down
- **Context preservation** - No more explaining the same project details repeatedly

**Automated Deflection:**
```text
Stakeholder: "Can we add real-time notifications?"
GitTalker: "That's outside my current knowledge scope - ask Mike directly for scope changes and timeline impact."

Stakeholder: "Why is this taking longer than expected?"
GitTalker: "Based on current timeline documentation, we're tracking to original estimates. For timeline concerns, please discuss directly with Mike."
```

**Developer Workflow Integration:**
```bash
# Mirror key docs to knowledge base
cp README.md .gittalker/gittalker/project-overview.md
cp CHANGELOG.md .gittalker/gittalker/progress-log.md

# Add daily controlled updates
echo "$(date): Authentication module completed" >> .gittalker/gittalker/daily-updates.md

# Stakeholders get updates, you stay focused
```

## 🔒 Security & Privacy

- **Sandboxed operation** - AI only accesses the `gittalker/` directory
- **No code exposure** - Your source code never leaves your repository  
- **Controlled information sharing** - You decide exactly what gets communicated
- **Audit trail** - All AI responses logged for review

This installer embeds the complete GitTalker AI agent service. The core service includes:

### Technical Architecture

- **FastAPI Backend** - High-performance async API for AI agent
- **Slack Integration** - Real-time client communication via Slack bot  
- **RAG Engine** - Intelligent search through your knowledge base
- **Multi-LLM Support** - OpenAI, Anthropic, Ollama, vLLM compatibility
- **Agent Personalities** - Customizable communication styles

### Development Setup (for GitTalker contributors)

```bash
# Clone the core service repository
git clone https://github.com/Immutablemike/gittalker.git
cd gittalker

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys

# Run the service
python src/main.py
```

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SLACK_BOT_TOKEN` | Bot User OAuth Token | ✅ |
| `SLACK_APP_TOKEN` | App-Level Token for Socket Mode | ✅ |
| `OPENAI_API_KEY` | OpenAI API key | One LLM required |
| `ANTHROPIC_API_KEY` | Anthropic API key | One LLM required |
| `GITHUB_TOKEN` | GitHub Personal Access Token | ✅ |
| `GITHUB_REPO_URL` | Repository URL to monitor | ✅ |
| `GITHUB_REPO_URL` | Repository URL to monitor | ✅ |

## 🤝 Contributing

**We welcome contributions!** 

- 🐛 **Bug reports** - Use GitHub Issues
- ✨ **Feature requests** - Discuss in GitHub Discussions  
- 🎭 **New agent personalities** - Submit via Pull Request
- 📚 **Documentation improvements** - Always appreciated

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details.

## 🆘 Support

- 💬 **GitHub Discussions** - Community help and questions
- 🐛 **GitHub Issues** - Bug reports and feature requests
- 📧 **Contact** - [@Immutablemike](https://github.com/Immutablemike) for direct support

---

**Ready to eliminate "What's the status?" interruptions?**

```bash
curl -fsSL https://raw.githubusercontent.com/Immutablemike/gittalker/main/INSTALL/install.sh | bash
```

*Built by developers, for developers who want to code in peace while keeping clients happy.* 🚀
```

### Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up --build

# Production deployment
docker-compose -f docker-compose.prod.yml up -d
```

## Architecture

GitTalker uses a hybrid architecture combining:

- **Agent Services** - Context-aware AI decision making (<50ms)
- **Direct Services** - High-performance computational tasks (<10ms)  
- **Hybrid Applications** - Intelligent coordination with automatic routing

This enables optimal performance across different use cases while maintaining intelligent behavior.

## Contributing

We welcome contributions! Please see:

- [Installation System](INSTALL/README.md) - Universal installer documentation
- [Core Service Development](src/README.md) - Backend service development
- [Issues](https://github.com/YourUsername/Gittalker/issues) - Bug reports and feature requests

## Support & Community

- 📖 **Documentation**: [Full installation guide](INSTALL/README.md)
- 🐛 **Issues**: [GitHub Issues](https://github.com/YourUsername/Gittalker/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/YourUsername/Gittalker/discussions)
- 📧 **Email**: support[at]gittalker.io

## License

MIT License - see [LICENSE](LICENSE) for details.
