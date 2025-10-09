# GitTalker Installation System Documentation

## Overview

The GitTalker installation system transforms any software project into an AI-powered development environment. It provides a universal companion that understands your codebase and offers intelligent assistance.

## Architecture

### Core Components

```
INSTALL/
├── install.sh              # Main installation script
├── README.md               # User documentation
├── test_installer.sh       # Validation test suite
├── templates/              # Project-specific configurations
│   ├── python.json         # Python project template
│   ├── javascript.json     # JavaScript/Node.js template
│   └── go.json             # Go project template
└── DEVELOPMENT.md          # This file
```

### Installation Flow

1. **Project Detection** - Analyzes project structure to determine type
2. **Template Selection** - Chooses appropriate configuration template
3. **Companion Setup** - Creates `.gittalker/` directory with client tools
4. **Integration** - Updates `.gitignore` and sets up local commands

### Generated Structure

```
your-project/
├── .gittalker/             # GitTalker companion directory
│   ├── config.json         # Project-specific configuration
│   ├── gittalker           # Executable client script
│   ├── knowledge/          # Indexed project files
│   │   └── file_index.json # Project file mapping
│   └── client/             # Python client module
│       └── __init__.py     # Client implementation
├── .gitignore              # Updated to ignore .gittalker/
└── [existing files]        # User's project remains untouched
```

## Project Detection Logic

The installer uses file-based heuristics to determine project type:

```bash
detect_project() {
    if [[ -f "package.json" ]]; then
        echo "javascript"
    elif [[ -f "requirements.txt" ]] || [[ -f "pyproject.toml" ]]; then
        echo "python"
    elif [[ -f "go.mod" ]]; then
        echo "go"
    elif [[ -f "Cargo.toml" ]]; then
        echo "rust"
    elif [[ -f "pom.xml" ]] || [[ -f "build.gradle" ]]; then
        echo "java"
    else
        echo "generic"
    fi
}
```

## Configuration Templates

Each project type has a JSON template that defines:

- **Scan patterns** - Which files to analyze
- **Ignore patterns** - Which files to skip
- **AI focus areas** - What the AI should prioritize
- **Framework hints** - Framework-specific file patterns

### Example Python Template Structure

```json
{
    "project_name": "python-project",
    "project_type": "python",
    "scan_patterns": {
        "python": ["**/*.py", "**/requirements.txt", "**/*.md"]
    },
    "ignore_patterns": ["__pycache__/**", "*.pyc", ".git/**"],
    "ai_focus_areas": ["code_quality", "performance_optimization"],
    "framework_hints": {
        "django": ["**/models.py", "**/views.py"],
        "fastapi": ["**/main.py", "**/routers/**"]
    }
}
```

## Client Interface

The generated client provides three main commands:

### Chat Mode
```bash
./gittalker chat
```
Interactive AI conversation about your project.

### Scan Mode
```bash
./gittalker scan
```
Analyzes and indexes project files for the AI.

### Documentation Mode
```bash
./gittalker docs
```
Generates comprehensive project documentation.

## Testing System

The test suite validates installation across different project types:

```bash
./test_installer.sh
```

### Test Coverage

- ✅ Python projects (FastAPI, Django, Flask)
- ✅ JavaScript projects (Node.js, React, Vue)
- ✅ Go projects (standard modules)
- ✅ Error conditions (non-git directories)
- ✅ File structure validation
- ✅ Client functionality verification

## Development Guidelines

### Adding New Project Types

1. **Add detection logic** in `install.sh`:
   ```bash
   elif [[ -f "new_marker_file" ]]; then
       echo "new_language"
   ```

2. **Create template** in `templates/new_language.json`:
   ```json
   {
       "project_type": "new_language",
       "scan_patterns": {"new_language": ["**/*.ext"]},
       "ignore_patterns": ["build/**"],
       "ai_focus_areas": ["language_specific_areas"]
   }
   ```

3. **Add test case** in `test_installer.sh`:
   ```bash
   test_installation "new_language"
   ```

### Client Extension

The Python client module can be extended with new capabilities:

```python
class GitTalkerClient:
    def new_feature(self):
        """Add new functionality here"""
        pass
```

### Configuration Options

Templates support these configuration keys:

- `project_name` - Auto-detected from directory
- `project_type` - Language/framework identifier  
- `scan_patterns` - File patterns to analyze
- `ignore_patterns` - File patterns to skip
- `ai_focus_areas` - AI specialization areas
- `framework_hints` - Framework detection patterns

## Security Considerations

### Local Processing
- Project files are analyzed locally
- No automatic upload to external services
- User controls what data is shared

### File Permissions
- Client scripts are executable only by owner
- Configuration files are readable only by owner
- Knowledge base is stored locally

### Git Integration
- Automatically adds `.gittalker/` to `.gitignore`
- Respects existing git configuration
- Does not modify project's git history

## Performance Optimization

### Scan Efficiency
- Configurable file patterns reduce scan time
- Intelligent ignore patterns skip large directories
- Batch processing for large codebases

### Memory Management
- Streaming file processing for large projects
- Configurable chunk limits for embeddings
- Lazy loading of project knowledge

## Future Enhancements

### Planned Features
- [ ] IDE integration (VS Code extension)
- [ ] Real-time file watching and re-indexing
- [ ] Multi-project knowledge sharing
- [ ] Custom AI model support
- [ ] Team collaboration features

### Architecture Evolution
- [ ] Plugin system for custom analysis
- [ ] API service for remote AI queries
- [ ] Web interface for project exploration
- [ ] Integration with popular development tools

## Troubleshooting

### Common Issues

**Installation fails with "Not in a git repository"**
- Solution: Run `git init` in your project directory

**Client commands don't work**
- Solution: Check file permissions with `ls -la .gittalker/gittalker`
- Fix: `chmod +x .gittalker/gittalker`

**Project type not detected correctly**
- Solution: Check your project has recognizable marker files
- Alternative: Manually edit `.gittalker/config.json`

### Debug Mode

Run installer with debug output:
```bash
bash -x install.sh
```

### Log Files

Client operations log to:
```
.gittalker/logs/client.log
```

## Contributing

### Pull Request Process

1. Add tests for new features
2. Update documentation
3. Ensure all tests pass
4. Follow commit message conventions

### Code Style

- Shell scripts: Follow [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html)
- Python: Follow PEP 8
- JSON: 2-space indentation

### Testing

Always run the test suite before submitting:
```bash
./test_installer.sh
```

---

**The GitTalker installation system makes AI assistance accessible to any software project with zero configuration and minimal overhead.**