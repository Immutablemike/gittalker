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
GITTALKER_REPO="https://github.com/YourUsername/Gittalker.git"
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

# Install GitTalker companion
install_gittalker() {
    local project_type=$1
    local project_name=$(basename "$(pwd)")
    
    log "Installing GitTalker companion for $project_type project: $project_name"
    
    # Create .gittalker directory
    if [[ -d "$GITTALKER_DIR" ]]; then
        warning "GitTalker already installed. Updating..."
        rm -rf "$GITTALKER_DIR"
    fi
    
    mkdir -p "$GITTALKER_DIR"
    
    # Clone GitTalker client template
    log "Setting up GitTalker client..."
    cat > "$GITTALKER_DIR/config.json" << EOF
{
    "project_name": "$project_name",
    "project_type": "$project_type",
    "gittalker_mode": "companion",
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
    
    # Create knowledge directory
    mkdir -p "$GITTALKER_DIR/knowledge"
    
    # Create client script
    cat > "$GITTALKER_DIR/gittalker" << 'EOF'
#!/bin/bash

# GitTalker Project Companion Client
# Quick access to your AI project assistant

GITTALKER_DIR=".gittalker"
CONFIG_FILE="config.json"

if [[ ! -f "$CONFIG_FILE" ]]; then
    echo "GitTalker not installed. Run: curl -fsSL https://install.gittalker.io | bash"
    exit 1
fi

# Parse command line arguments
case "${1:-help}" in
    "chat"|"c")
        echo "Starting GitTalker chat session..."
        python3 client/__init__.py --mode=chat
        ;;
    "scan"|"s")
        echo "Scanning project for GitTalker..."
        python3 client/__init__.py --mode=scan
        ;;
    "docs"|"d")
        echo "Generating project documentation..."
        python3 client/__init__.py --mode=docs
        ;;
    "help"|"h"|*)
        echo "GitTalker Project Companion"
        echo ""
        echo "Usage:"
        echo "  ./gittalker chat   - Start interactive chat session"
        echo "  ./gittalker scan   - Scan and index project files"
        echo "  ./gittalker docs   - Generate project documentation"
        echo "  ./gittalker help   - Show this help"
        echo ""
        echo "Quick commands:"
        echo "  ./gittalker c      - Chat (shorthand)"
        echo "  ./gittalker s      - Scan (shorthand)"
        echo "  ./gittalker d      - Docs (shorthand)"
        ;;
esac
EOF
    
    chmod +x "$GITTALKER_DIR/gittalker"
    
    # Create Python client module
    mkdir -p "$GITTALKER_DIR/client"
    cat > "$GITTALKER_DIR/client/__init__.py" << 'EOF'
"""
GitTalker Project Companion Client
Lightweight interface to GitTalker AI assistant
"""

import os
import sys
import json
import glob
import argparse
from pathlib import Path

class GitTalkerClient:
    def __init__(self, config_path="config.json"):
        self.config_path = config_path
        self.config = self.load_config()
        self.knowledge_dir = Path("knowledge")
        
    def load_config(self):
        """Load GitTalker configuration"""
        try:
            with open(self.config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("GitTalker config not found. Run installer first.")
            sys.exit(1)
            
    def scan_project(self):
        """Scan project files and build knowledge base"""
        print(f"Scanning {self.config['project_type']} project: {self.config['project_name']}")
        
        patterns = self.config['scan_patterns'].get(self.config['project_type'], [])
        ignore = self.config['ignore_patterns']
        
        # Change to parent directory to scan the actual project
        os.chdir('..')
        
        files_found = []
        for pattern in patterns:
            files = glob.glob(pattern, recursive=True)
            for file in files:
                if not any(ignored in file for ignored in ignore):
                    files_found.append(file)
        
        print(f"Found {len(files_found)} relevant files")
        
        # Create knowledge index (in .gittalker/knowledge/)
        knowledge_dir = Path(".gittalker/knowledge")
        knowledge_dir.mkdir(exist_ok=True)
        with open(knowledge_dir / "file_index.json", 'w') as f:
            json.dump({
                "project": self.config['project_name'],
                "type": self.config['project_type'],
                "files": files_found,
                "last_scan": str(Path.cwd())
            }, f, indent=2)
            
        print("Knowledge base updated!")
        
    def start_chat(self):
        """Start interactive chat session"""
        print("GitTalker Chat Mode - Your AI Project Companion")
        print("Type 'exit' to quit, 'help' for commands")
        print("-" * 50)
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if user_input.lower() in ['exit', 'quit']:
                    print("Goodbye!")
                    break
                elif user_input.lower() == 'help':
                    self.show_chat_help()
                elif user_input:
                    # In a full implementation, this would connect to GitTalker API
                    self.mock_response(user_input)
                    
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
                
    def mock_response(self, query):
        """Mock AI response (replace with actual GitTalker API call)"""
        responses = [
            f"I understand you're asking about: '{query}' in your {self.config['project_type']} project.",
            "I'm analyzing your project structure and codebase...",
            "Based on your project, here are some suggestions:",
            "Would you like me to help with code review, documentation, or testing?"
        ]
        
        import random
        print(f"GitTalker: {random.choice(responses)}")
        
    def show_chat_help(self):
        """Show chat commands"""
        print("\nGitTalker Chat Commands:")
        print("  help     - Show this help")
        print("  scan     - Rescan project files")
        print("  files    - List indexed files")
        print("  config   - Show project config")
        print("  exit     - Quit chat")
        print()
        
    def generate_docs(self):
        """Generate project documentation"""
        print("Generating project documentation...")
        print("This would analyze your code and create comprehensive docs!")
        
def main():
    parser = argparse.ArgumentParser(description='GitTalker Project Companion')
    parser.add_argument('--mode', choices=['chat', 'scan', 'docs'], 
                       default='chat', help='Operation mode')
    
    args = parser.parse_args()
    client = GitTalkerClient()
    
    if args.mode == 'chat':
        client.start_chat()
    elif args.mode == 'scan':
        client.scan_project()
    elif args.mode == 'docs':
        client.generate_docs()

if __name__ == '__main__':
    main()
EOF
    
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
    
    success "GitTalker companion installed successfully!"
    echo ""
    echo "Quick start:"
    echo "  cd $GITTALKER_DIR && ./gittalker chat"
    echo "  cd $GITTALKER_DIR && ./gittalker scan"
    echo ""
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
    echo "🎉 Installation complete!"
    echo ""
    echo "Next steps:"
    echo "1. cd .gittalker"
    echo "2. ./gittalker scan    # Index your project"
    echo "3. ./gittalker chat    # Start AI companion"
    echo ""
    echo "Need help? Check: https://docs.gittalker.io"
}

# Run if executed directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi