#!/bin/bash

# Simple deployment script
echo "🚀 Deploying DocsBot..."

# Check if .env exists
if [ ! -f .env ]; then
    echo "❌ .env file not found. Please copy .env.example to .env and configure your API keys."
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Test configuration
echo "🔧 Testing configuration..."
python -c "
from src.config import OPENAI_API_KEY, GITHUB_TOKEN, SLACK_BOT_TOKEN, SLACK_APP_TOKEN
import sys

missing = []
if not OPENAI_API_KEY: missing.append('OPENAI_API_KEY')
if not GITHUB_TOKEN: missing.append('GITHUB_TOKEN')  
if not SLACK_BOT_TOKEN: missing.append('SLACK_BOT_TOKEN')
if not SLACK_APP_TOKEN: missing.append('SLACK_APP_TOKEN')

if missing:
    print(f'❌ Missing environment variables: {missing}')
    sys.exit(1)
else:
    print('✅ All environment variables configured')
"

if [ $? -ne 0 ]; then
    exit 1
fi

# Start the bot
echo "🤖 Starting DocsBot..."
python -m uvicorn src.main:app --host 0.0.0.0 --port 8000