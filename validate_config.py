# GitTalker Configuration Validation
import os
import sys
from typing import List, Tuple


def validate_config() -> Tuple[bool, List[str]]:
    """Validate GitTalker configuration."""
    validation_errors = []
    
    # Required environment variables
    required_vars = [
        "OPENAI_API_KEY",
        "GITHUB_TOKEN",
        "GITHUB_REPO",
        "SLACK_BOT_TOKEN",
        "SLACK_APP_TOKEN"
    ]
    
    # Check for missing variables
    for var in required_vars:
        if not os.getenv(var):
            validation_errors.append(
                f"Missing required environment variable: {var}"
            )
    
    # Validate GitHub repo format
    github_repo = os.getenv("GITHUB_REPO", "")
    if github_repo and "/" not in github_repo:
        validation_errors.append("GITHUB_REPO must be in format 'owner/repo'")
    
    # Validate OpenAI API key format
    openai_key = os.getenv("OPENAI_API_KEY", "")
    if openai_key and not openai_key.startswith("sk-"):
        validation_errors.append("OPENAI_API_KEY appears to be invalid format")
    
    # Validate Slack tokens
    slack_bot = os.getenv("SLACK_BOT_TOKEN", "")
    if slack_bot and not slack_bot.startswith("xoxb-"):
        validation_errors.append(
            "SLACK_BOT_TOKEN appears to be invalid format"
        )
        
    slack_app = os.getenv("SLACK_APP_TOKEN", "")
    if slack_app and not slack_app.startswith("xapp-"):
        validation_errors.append(
            "SLACK_APP_TOKEN appears to be invalid format"
        )
    
    return len(validation_errors) == 0, validation_errors


if __name__ == "__main__":
    print("🔍 Validating GitTalker configuration...")
    
    # Load .env file if it exists
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        print("⚠️ python-dotenv not installed, skipping .env file loading")
    
    is_valid, errors = validate_config()
    
    if is_valid:
        print("✅ Configuration is valid!")
        sys.exit(0)
    else:
        print("❌ Configuration errors found:")
        for error in errors:
            print(f"   - {error}")
        print("\n💡 Please check your .env file and fix the above issues")
        sys.exit(1)
