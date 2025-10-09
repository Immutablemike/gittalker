#!/bin/bash

# GitTalker Installer Test Suite
# Validates installation across different project types

set -euo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Test configuration
TEST_DIR="$(mktemp -d)"
INSTALLER_PATH="$(pwd)/install.sh"
PASSED=0
FAILED=0

log() { echo -e "${BLUE}[TEST]${NC} $1"; }
success() { echo -e "${GREEN}[PASS]${NC} $1"; ((PASSED++)); }
fail() { echo -e "${RED}[FAIL]${NC} $1"; ((FAILED++)); }

# Create test project
create_test_project() {
    local project_type=$1
    local project_name="test-$project_type-project"
    local project_dir="$TEST_DIR/$project_name"
    
    mkdir -p "$project_dir"
    cd "$project_dir"
    
    # Initialize git
    git init --quiet
    git config user.email "test@gittalker.io"
    git config user.name "Test User"
    
    # Create project-specific files
    case $project_type in
        "python")
            cat > requirements.txt << EOF
fastapi==0.104.1
uvicorn==0.24.0
pydantic==2.5.0
EOF
            cat > main.py << 'EOF'
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello GitTalker!"}
EOF
            ;;
        "javascript")
            cat > package.json << EOF
{
    "name": "$project_name",
    "version": "1.0.0",
    "dependencies": {
        "express": "^4.18.0"
    }
}
EOF
            cat > index.js << 'EOF'
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.json({ message: 'Hello GitTalker!' });
});

app.listen(3000);
EOF
            ;;
        "go")
            cat > go.mod << EOF
module $project_name

go 1.21
EOF
            cat > main.go << 'EOF'
package main

import "fmt"

func main() {
    fmt.Println("Hello GitTalker!")
}
EOF
            ;;
    esac
    
    # Create README
    cat > README.md << EOF
# $project_name

Test project for GitTalker installer validation.
EOF
    
    git add .
    git commit -m "Initial commit" --quiet
    
    echo "$project_dir"
}

# Test installation
test_installation() {
    local project_type=$1
    local project_dir=$(create_test_project "$project_type")
    
    log "Testing $project_type project installation..."
    
    cd "$project_dir"
    
    # Run installer
    if bash "$INSTALLER_PATH" > /dev/null 2>&1; then
        success "Installer ran successfully for $project_type"
    else
        fail "Installer failed for $project_type"
        return
    fi
    
    # Check .gittalker directory
    if [[ -d ".gittalker" ]]; then
        success ".gittalker directory created"
    else
        fail ".gittalker directory not created"
        return
    fi
    
    # Check config file
    if [[ -f ".gittalker/config.json" ]]; then
        success "config.json created"
        
        # Validate config content
        if grep -q "\"project_type\": \"$project_type\"" .gittalker/config.json; then
            success "Project type correctly detected as $project_type"
        else
            fail "Project type incorrectly detected"
        fi
    else
        fail "config.json not created"
    fi
    
    # Check client script
    if [[ -x ".gittalker/gittalker" ]]; then
        success "GitTalker client script created and executable"
    else
        fail "GitTalker client script not created or not executable"
    fi
    
    # Check .gitignore
    if [[ -f ".gitignore" ]] && grep -q ".gittalker" .gitignore; then
        success ".gitignore updated with .gittalker entry"
    else
        fail ".gitignore not updated"
    fi
    
    # Test client functionality
    cd .gittalker
    if ./gittalker help > /dev/null 2>&1; then
        success "GitTalker client help command works"
    else
        fail "GitTalker client help command failed"
    fi
    
    log "Completed tests for $project_type"
    echo ""
}

# Test error conditions
test_error_conditions() {
    log "Testing error conditions..."
    
    # Test non-git directory
    local non_git_dir="$TEST_DIR/non-git"
    mkdir -p "$non_git_dir"
    cd "$non_git_dir"
    
    if bash "$INSTALLER_PATH" 2>&1 | grep -q "Not in a git repository"; then
        success "Correctly rejects non-git directory"
    else
        fail "Should reject non-git directory"
    fi
    
    log "Error condition tests completed"
    echo ""
}

# Main test runner
main() {
    log "Starting GitTalker installer test suite"
    log "Test directory: $TEST_DIR"
    echo ""
    
    # Test different project types
    test_installation "python"
    test_installation "javascript" 
    test_installation "go"
    
    # Test error conditions
    test_error_conditions
    
    # Summary
    log "Test Results:"
    echo "  Passed: $PASSED"
    echo "  Failed: $FAILED"
    echo ""
    
    if [[ $FAILED -eq 0 ]]; then
        success "All tests passed! 🎉"
        exit 0
    else
        fail "Some tests failed"
        exit 1
    fi
}

# Cleanup
cleanup() {
    rm -rf "$TEST_DIR"
}
trap cleanup EXIT

# Run tests
main "$@"