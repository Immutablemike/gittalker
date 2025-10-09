# GitTalker Universal Project Companion

**Drop-in AI assistant for any software project**

## 🚀 One-Line Installation

```bash
curl -fsSL https://install.gittalker.io | bash
```

*Or download and run locally:*

```bash
git clone https://github.com/YourUsername/Gittalker.git
cd Gittalker/INSTALL
./install.sh
```

## What This Does

GitTalker becomes your **intelligent project companion** that:

- 🧠 **Understands your codebase** - Automatically scans and indexes your project files
- 💬 **Provides instant help** - Chat interface for code questions, debugging, and suggestions  
- 📚 **Generates documentation** - Creates comprehensive docs from your code
- 🔍 **Code analysis** - Reviews code quality, suggests improvements
- 🏗️ **Architecture insights** - Understands your project structure and patterns

## Supported Project Types

✅ **Python** - Django, Flask, FastAPI, pip, poetry  
✅ **JavaScript/TypeScript** - Node.js, React, Vue, Angular, npm, yarn  
✅ **Go** - Standard Go projects with go.mod  
✅ **Rust** - Cargo-based projects  
✅ **Java** - Maven, Gradle projects  
✅ **PHP** - Composer projects  
✅ **Generic** - Any project with documentation  

## How It Works

### 1. Smart Detection
GitTalker automatically detects your project type by analyzing:
- Package files (`package.json`, `requirements.txt`, `go.mod`, etc.)
- Project structure and file patterns
- Build configurations

### 2. Lightweight Installation
Creates a `.gittalker/` directory in your project with:
- **Companion client** - Lightweight interface to GitTalker AI
- **Project config** - Customized for your specific project type
- **Knowledge base** - Indexed project files and documentation
- **Chat interface** - Interactive AI assistant

### 3. Zero Interference
- Adds only one directory (`.gittalker/`) to your project
- Automatically adds to `.gitignore`
- No modifications to your existing code
- Works alongside any existing tools

## Quick Start Guide

After installation, you get these commands:

```bash
# Enter GitTalker directory
cd .gittalker

# Scan and index your project
./gittalker scan

# Start interactive chat with AI
./gittalker chat

# Generate project documentation  
./gittalker docs
```

### Example Chat Session

```
$ ./gittalker chat
GitTalker Chat Mode - Your AI Project Companion
Type 'exit' to quit, 'help' for commands
--------------------------------------------------

You: How can I improve the performance of my API?
GitTalker: I've analyzed your FastAPI project. Here are specific optimizations for your codebase:

1. Add async/await to your database queries in src/models.py
2. Implement response caching for your /api/users endpoint
3. Consider connection pooling for your PostgreSQL database

Would you like me to show you the specific code changes?

You: Yes, show me the async database changes
GitTalker: Here's how to update your User model in src/models.py:

[Shows specific code examples based on your actual files]
```

## Installation Details

### What Gets Created

```
your-project/
├── .gittalker/           # GitTalker companion directory
│   ├── config.json       # Project-specific configuration
│   ├── gittalker         # Executable client script
│   ├── knowledge/        # Indexed project files
│   └── client/           # Python client module
├── .gitignore            # Updated to ignore .gittalker/
└── [your existing files] # Untouched
```

### Configuration Example

```json
{
    "project_name": "my-awesome-app",
    "project_type": "python",
    "gittalker_mode": "companion",
    "scan_patterns": {
        "python": ["**/*.py", "**/requirements.txt", "**/pyproject.toml"]
    },
    "ignore_patterns": [
        "node_modules/**", "__pycache__/**", ".git/**"
    ]
}
```

## Advanced Usage

### Custom Scan Patterns

Edit `.gittalker/config.json` to customize which files GitTalker analyzes:

```json
{
    "scan_patterns": {
        "python": [
            "**/*.py",
            "**/requirements.txt", 
            "**/README.md",
            "**/docs/**/*.md"
        ]
    }
}
```

### Command Line Options

```bash
# Full commands
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
# Now your project is indexed and ready for AI queries
```

## Requirements

- **Git repository** - Must be run from within a git project
- **Python 3.7+** - For the client interface
- **Internet connection** - To communicate with GitTalker AI service

## Troubleshooting

### Installation Issues

```bash
# Check if you're in a git repository
git status

# Ensure script is executable
chmod +x INSTALL/install.sh

# Run with debug output
bash -x INSTALL/install.sh
```

### Common Problems

**"Not in a git repository"**
- Run `git init` in your project directory first
- Make sure you're in the project root directory

**"GitTalker config not found"**
- Re-run the installer: `./install.sh`
- Check that `.gittalker/config.json` exists

**"Permission denied"**
- Make client executable: `chmod +x .gittalker/gittalker`

## Security & Privacy

- **Local processing** - Project files are analyzed locally
- **Secure communication** - Encrypted connection to GitTalker AI service
- **No code storage** - Your code is not stored on external servers
- **Opt-in sharing** - You control what information is sent to the AI

## Uninstalling

To remove GitTalker from your project:

```bash
# Remove GitTalker directory
rm -rf .gittalker

# Remove from .gitignore (optional)
sed -i '' '/\.gittalker/d' .gitignore
```

## Examples

### Python Django Project
```bash
# Detected as Python project
# Scans: *.py, requirements.txt, manage.py, settings/
# Provides: Django-specific advice, ORM optimization, security tips
```

### Node.js React App
```bash
# Detected as JavaScript project  
# Scans: *.js, *.tsx, package.json, public/, src/
# Provides: React patterns, npm optimization, build improvements
```

### Go Microservice
```bash
# Detected as Go project
# Scans: *.go, go.mod, go.sum, cmd/, internal/
# Provides: Go best practices, performance tips, concurrency advice
```

## Contributing

Want to improve GitTalker's project detection or add support for new languages?

1. Fork the repository
2. Add detection patterns in `install.sh`
3. Test with real projects
4. Submit a pull request

## Support

- 📖 **Documentation**: https://docs.gittalker.io
- 🐛 **Issues**: https://github.com/YourUsername/Gittalker/issues
- 💬 **Discussions**: https://github.com/YourUsername/Gittalker/discussions
- 📧 **Email**: support@gittalker.io

---

**Made with ❤️ for developers who want AI-powered project companions**