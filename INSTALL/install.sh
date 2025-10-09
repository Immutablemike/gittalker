#!/bin/bash

# GitTalker Universal Project Companion Installer
# Drop-in AI assistant for any software project

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
GITTALKER_REPO="https://github.com/Immutablemike/gittalker.git"
GITTALKER_DIR=".gittalker"
CLIENT_DIR="gittalker-client"

# Logging function
log() {
    echo -e "${BLUE}[GitTalker]${NC} $1"
}

success() {
    echo -e "${GREEN}[GitTalker]${NC} $1"
}

warning() {
    echo -e "${YELLOW}[GitTalker]${NC} $1"
}

error() {
    echo -e "${RED}[GitTalker]${NC} $1"
    exit 1
}

# Check if we're in a git repository
check_git_repo() {
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        error "Not in a git repository. Please run this from your project root."
    fi
}

# Detect project type and language
detect_project() {
    if [[ -f "package.json" ]]; then
        echo "javascript"
    elif [[ -f "requirements.txt" ]] || [[ -f "pyproject.toml" ]] || [[ -f "setup.py" ]]; then
        echo "python"
    elif [[ -f "go.mod" ]]; then
        echo "go"
    elif [[ -f "Cargo.toml" ]]; then
        echo "rust"
    elif [[ -f "pom.xml" ]] || [[ -f "build.gradle" ]]; then
        echo "java"
    elif [[ -f "composer.json" ]]; then
        echo "php"
    else
        echo "generic"
    fi
}

# Install GitTalker AI agent service
install_gittalker() {
    local project_type=$1
    local project_name=$(basename "$(pwd)")
    
    log "Installing GitTalker AI agent for $project_type project: $project_name"
    
    # Create .gittalker directory
    if [[ -d "$GITTALKER_DIR" ]]; then
        warning "GitTalker already installed. Updating..."
        rm -rf "$GITTALKER_DIR"
    fi
    
    mkdir -p "$GITTALKER_DIR"
    
    # Clone GitTalker source code
    log "Downloading GitTalker AI agent..."
    git clone --depth 1 "$GITTALKER_REPO" "$GITTALKER_DIR/gittalker-source" 2>/dev/null || {
        error "Failed to download GitTalker. Check internet connection."
    }
    
    # Copy core GitTalker files
    log "Installing GitTalker service..."
    cp -r "$GITTALKER_DIR/gittalker-source/src" "$GITTALKER_DIR/"
    cp "$GITTALKER_DIR/gittalker-source/requirements.txt" "$GITTALKER_DIR/"
    cp -r "$GITTALKER_DIR/gittalker-source/AGENT_Profiles" "$GITTALKER_DIR/"
    
    # Create .env template
    cat > "$GITTALKER_DIR/.env.example" << 'EOF'
# Slack Configuration
SLACK_BOT_TOKEN=xoxb-your-slack-bot-token
SLACK_APP_TOKEN=xapp-your-app-level-token

# LLM Provider (choose one)
OPENAI_API_KEY=sk-your-openai-key
# ANTHROPIC_API_KEY=sk-ant-your-anthropic-key
# OLLAMA_BASE_URL=http://localhost:11434
# VLLM_BASE_URL=http://localhost:8000

# GitHub Configuration
GITHUB_TOKEN=ghp_your-github-token
GITHUB_REPO_URL=https://github.com/yourusername/your-repo

# Agent Configuration
AGENT_PROFILE=AGENT_Profiles/mike_jive_robot.json
REPO_SCOPE_PATH=gittalker/
EOF

    # Create starter knowledge base
    mkdir -p "$GITTALKER_DIR/gittalker"
    cat > "$GITTALKER_DIR/gittalker/README.md" << EOF
# $project_name Knowledge Base

This directory contains documentation that your GitTalker AI agent will use to answer questions about your project.

## What to include:

- **Project overview** - What does this project do?
- **Current status** - What's in progress, what's complete?
- **Roadmap** - Upcoming features and timeline
- **FAQ** - Common client questions and answers
- **Technical specs** - Implementation details (if clients need them)

## Example structure:

\`\`\`
gittalker/
├── README.md (this file)
├── project-overview.md
├── current-status.md
├── roadmap.md
├── faq.md
└── technical-specs.md
\`\`\`

Your GitTalker AI will read these files and answer client questions based on this information.
EOF

    cat > "$GITTALKER_DIR/gittalker/project-overview.md" << EOF
# $project_name Project Overview

## What We're Building

[Describe your project - what problem does it solve? Who is it for?]

## Key Features

- [ ] Feature 1 - [Status: Not started/In progress/Complete]
- [ ] Feature 2 - [Status: Not started/In progress/Complete]  
- [ ] Feature 3 - [Status: Not started/In progress/Complete]

## Technology Stack

**Backend:** [Your backend tech]
**Frontend:** [Your frontend tech]
**Database:** [Your database]
**Deployment:** [Your hosting solution]

## Timeline

**Project Start:** [Date]
**Expected Launch:** [Date]
**Current Phase:** [Phase description]

---
*Last updated: $(date)*
EOF

    cat > "$GITTALKER_DIR/gittalker/faq.md" << EOF
# $project_name - Frequently Asked Questions

## General Questions

**Q: What does this project do?**
A: [Brief description of your project's purpose and value]

**Q: When will it be ready?**
A: [Timeline information and current status]

**Q: What features are included?**
A: [List of confirmed features for this project]

**Q: What's NOT included in this project?**
A: [Important - be clear about scope boundaries]

## Technical Questions

**Q: What technology are you using?**
A: [Brief tech stack overview appropriate for clients]

**Q: Will this work on mobile?**
A: [Mobile compatibility information]

**Q: How secure is this?**
A: [Security measures and compliance info]

## Project Management

**Q: How can I track progress?**
A: Ask @GitTalker for status updates anytime in this channel!

**Q: Who do I contact for urgent issues?**
A: [Contact information for escalation]

**Q: Can I request changes or new features?**
A: [Process for handling change requests]

---
*This FAQ is updated regularly. Ask @GitTalker if you have other questions!*
EOF
    
    # Create project configuration
    cat > "$GITTALKER_DIR/config.json" << EOF
{
    "project_name": "$project_name",
    "project_type": "$project_type",
    "gittalker_mode": "service",
    "knowledge_base_path": "gittalker/",
    "agent_profile": "AGENT_Profiles/mike_jive_robot.json",
    "scan_patterns": {
        "python": ["**/*.py", "**/requirements.txt", "**/pyproject.toml"],
        "javascript": ["**/*.js", "**/*.ts", "**/package.json", "**/README.md"],
        "go": ["**/*.go", "**/go.mod", "**/go.sum"],
        "rust": ["**/*.rs", "**/Cargo.toml"],
        "java": ["**/*.java", "**/pom.xml", "**/build.gradle"],
        "php": ["**/*.php", "**/composer.json"],
        "generic": ["**/*.md", "**/README*", "**/docs/**"]
    },
    "ignore_patterns": [
        "node_modules/**",
        "__pycache__/**",
        ".git/**",
        "*.pyc",
        "*.log",
        "dist/**",
        "build/**",
        ".gittalker/**"
    ]
}
EOF
    
    # Create GitTalker startup script
    cat > "$GITTALKER_DIR/start-gittalker.sh" << 'EOF'
#!/bin/bash

# GitTalker AI Agent Startup Script
cd "$(dirname "$0")"

echo "🤖 Starting GitTalker AI Agent..."

# Check if .env exists
if [[ ! -f ".env" ]]; then
    echo "❌ .env file not found!"
    echo "📋 Copy .env.example to .env and configure your API keys:"
    echo "   cp .env.example .env"
    echo "   nano .env"
    exit 1
fi

# Check if Python dependencies are installed
if ! python3 -c "import fastapi, slack_sdk, openai" 2>/dev/null; then
    echo "📦 Installing Python dependencies..."
    pip3 install -r requirements.txt
fi

# Start GitTalker service
echo "🚀 GitTalker AI Agent is running..."
echo "💬 Your AI agent is now listening in Slack!"
echo "📚 Knowledge base: gittalker/ directory"
echo "🛑 Press Ctrl+C to stop"
echo ""

python3 src/main.py
EOF

    chmod +x "$GITTALKER_DIR/start-gittalker.sh"
    
    # Create quick management script
    cat > "$GITTALKER_DIR/gittalker" << 'EOF'
#!/bin/bash

# GitTalker AI Agent Management Script
GITTALKER_DIR="$(dirname "$0")"
cd "$GITTALKER_DIR"

case "${1:-help}" in
    "start"|"run")
        echo "🚀 Starting GitTalker AI Agent..."
        ./start-gittalker.sh
        ;;
    "stop")
        echo "🛑 Stopping GitTalker..."
        pkill -f "python3 src/main.py" || echo "GitTalker not running"
        ;;
    "status")
        if pgrep -f "python3 src/main.py" > /dev/null; then
            echo "✅ GitTalker AI Agent is running"
        else
            echo "❌ GitTalker AI Agent is not running"
        fi
        ;;
    "logs")
        echo "📋 GitTalker logs (press Ctrl+C to exit):"
        tail -f logs/gittalker.log 2>/dev/null || echo "No logs found yet"
        ;;
    "config")
        echo "⚙️ Opening configuration..."
        ${EDITOR:-nano} .env
        ;;
    "knowledge")
        echo "📚 Opening knowledge base..."
        ${EDITOR:-nano} gittalker/README.md
        ;;
    "profiles")
        echo "🎭 Available agent profiles:"
        ls -1 AGENT_Profiles/*.json | sed 's/.*\//  - /'
        echo ""
        echo "Current profile: $(grep agent_profile config.json | cut -d'"' -f4)"
        ;;
    "help"|*)
        echo "GitTalker AI Agent Management"
        echo ""
        echo "Usage: ./gittalker <command>"
        echo ""
        echo "Commands:"
        echo "  start      - Start GitTalker AI agent service"
        echo "  stop       - Stop GitTalker AI agent"
        echo "  status     - Check if GitTalker is running"
        echo "  logs       - View GitTalker logs"
        echo "  config     - Edit configuration (.env file)"
        echo "  knowledge  - Edit knowledge base"
        echo "  profiles   - List available agent personalities"
        echo "  help       - Show this help"
        echo ""
        echo "Quick Setup:"
        echo "  1. ./gittalker config    # Add your API keys"
        echo "  2. ./gittalker knowledge # Update project info"
        echo "  3. ./gittalker start     # Launch your AI agent"
        ;;
esac
EOF
        "dist/**",
    
    chmod +x "$GITTALKER_DIR/gittalker"
    
    # Clean up downloaded source (keep only what we need)
    rm -rf "$GITTALKER_DIR/gittalker-source"
    
    # Create logs directory
    mkdir -p "$GITTALKER_DIR/logs"
    
    # Add to .gitignore
    if [[ -f ".gitignore" ]]; then
        if ! grep -q ".gittalker" .gitignore; then
            echo ".gittalker/" >> .gitignore
            log "Added .gittalker/ to .gitignore"
        fi
    else
        echo ".gittalker/" > .gitignore
        log "Created .gitignore with .gittalker/ entry"
    fi
    
    success "GitTalker AI Agent installed successfully!"
    echo ""
    echo "🎉 Your AI agent is ready!"
    echo ""
    echo "📋 Next steps:"
    echo "1. cd .gittalker"
    echo "2. ./gittalker config      # Add your API keys & Slack bot"
    echo "3. ./gittalker knowledge   # Update project information" 
    echo "4. ./gittalker start       # Launch your AI agent"
    echo ""
    echo "📚 Knowledge base created at: .gittalker/gittalker/"
    echo "🎭 Agent profiles available at: .gittalker/AGENT_Profiles/"
    echo ""
    echo "💡 Your AI agent will answer client questions based on the"
    echo "   documentation in the gittalker/ folder."
}

# Main installation flow
main() {
    log "GitTalker Universal Project Companion Installer"
    echo "Drop-in AI assistant for any software project"
    echo ""
    
    # Checks
    check_git_repo
    
    # Detect project
    project_type=$(detect_project)
    log "Detecting project type..."
    success "Detected project type: $project_type"
    
    # Install
    install_gittalker "$project_type"
    
    # Final instructions
    echo ""
    echo "🎉 GitTalker AI Agent Installation Complete!"
    echo ""
    echo "📋 Quick Setup:"
    echo "1. cd .gittalker"
    echo "2. ./gittalker config      # Add API keys & Slack bot tokens"
    echo "3. ./gittalker knowledge   # Customize project documentation"
    echo "4. ./gittalker start       # Launch your AI agent"
    echo ""
    echo "🤖 Your AI agent will be embedded in Slack, ready to answer"
    echo "   client questions about your project based on the knowledge"
    echo "   base in the gittalker/ directory."
    echo ""
    echo "💬 Invite your GitTalker bot to Slack channels and clients"
    echo "   can ask questions anytime with @GitTalker"
    echo ""
    echo "📖 Documentation: https://docs.gittalker.io"
}

# Run if executed directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi