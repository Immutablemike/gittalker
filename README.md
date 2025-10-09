# GitTalker - Universal AI Project Companion

**Drop-in AI assistant for any software project**

## 🚀 One-Line Installation

```bash
curl -fsSL https://install.gittalker.io | bash
```

GitTalker becomes your intelligent project companion - understanding your codebase, providing instant help, and generating documentation automatically.

## What GitTalker Does

🧠 **Understands Your Codebase** - Automatically scans and indexes your project files  
💬 **Provides Instant Help** - Chat interface for code questions, debugging, and suggestions  
📚 **Generates Documentation** - Creates comprehensive docs from your code  
🔍 **Code Analysis** - Reviews code quality, suggests improvements  
🏗️ **Architecture Insights** - Understands your project structure and patterns  

## Supported Projects

✅ **Python** - Django, Flask, FastAPI, pip, poetry  
✅ **JavaScript/TypeScript** - Node.js, React, Vue, Angular, npm, yarn  
✅ **Go** - Standard Go projects with go.mod  
✅ **Rust** - Cargo-based projects  
✅ **Java** - Maven, Gradle projects  
✅ **PHP** - Composer projects  
✅ **Any Project** - Generic documentation and analysis  

## Quick Start

After running the installer in your project:

```bash
# Enter GitTalker companion
cd .gittalker

# Scan and index your project  
./gittalker scan

# Start AI chat session
./gittalker chat

# Generate documentation
./gittalker docs
```

### Example Chat Session

```
You: How can I improve the performance of my API?
GitTalker: I've analyzed your FastAPI project. Here are specific optimizations:

1. Add async/await to your database queries in src/models.py
2. Implement response caching for your /api/users endpoint  
3. Consider connection pooling for your PostgreSQL database

Would you like me to show you the specific code changes?

You: Yes, show me the async database changes
GitTalker: Here's how to update your User model in src/models.py:
[Shows specific code examples based on your actual files]
```

## How It Works

### 1. Smart Detection
Automatically detects your project type by analyzing package files, project structure, and build configurations.

### 2. Lightweight Installation  
Creates a single `.gittalker/` directory with:
- Companion client for AI interaction
- Project-specific configuration  
- Local knowledge base of your code
- Interactive chat interface

### 3. Zero Interference
- Adds only one directory to your project
- Automatically updates `.gitignore`
- No modifications to existing code
- Works alongside any existing tools

## Installation Details

The installer creates this structure in your project:

```
your-project/
├── .gittalker/           # GitTalker companion directory
│   ├── config.json       # Project-specific configuration
│   ├── gittalker         # Executable client script  
│   ├── knowledge/        # Indexed project files
│   └── client/           # Python client module
├── .gitignore            # Updated to ignore .gittalker/
└── [your files]          # Completely untouched
```

## Advanced Usage

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

```python
from gittalker.client import GitTalkerClient

client = GitTalkerClient()
client.scan_project()
# Project is now indexed and ready for AI queries
```

## GitTalker Core Service

This repository also contains the core GitTalker service that powers the AI companion:

### Core Features
- **FastAPI Backend** - High-performance async API
- **Slack Integration** - Real-time chat interface  
- **RAG Engine** - Intelligent document search and retrieval
- **GitHub Integration** - Automatic documentation fetching
- **Multi-Personality AI** - Configurable AI personalities

### Development Setup

```bash
# Clone repository
git clone https://github.com/YourUsername/Gittalker.git
cd Gittalker

# Install dependencies  
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys

# Run development server
uvicorn src.main:app --reload
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

## Requirements

- **Git repository** - Must be run from within a git project
- **Python 3.7+** - For the companion client interface
- **Internet connection** - To communicate with GitTalker AI service

## Security & Privacy

- **Local processing** - Project files analyzed locally
- **Secure communication** - Encrypted connection to AI service
- **No code storage** - Your code is not stored on external servers
- **Opt-in sharing** - You control what information is sent

## Contributing

We welcome contributions! Please see:

- [Installation System](INSTALL/README.md) - Universal installer documentation
- [Core Service](src/README.md) - Backend service development
- [Issues](https://github.com/YourUsername/Gittalker/issues) - Bug reports and feature requests

## Support

- 📖 **Documentation**: [Full installation guide](INSTALL/README.md)
- 🐛 **Issues**: [GitHub Issues](https://github.com/YourUsername/Gittalker/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/YourUsername/Gittalker/discussions)
- 📧 **Email**: support@gittalker.io

## License

MIT License - see [LICENSE](LICENSE) for details.

---

**Turn any project into an AI-powered development environment with GitTalker**

*Made with ❤️ for developers who want intelligent coding companions*