#!/bin/bash
# GitTalker Environment Setup Script

echo "🚀 Setting up GitTalker environment..."

# Check Python version
python3 --version
if [ $? -ne 0 ]; then
    echo "❌ Python 3 is required but not installed"
    exit 1
fi

# Create virtual environment
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p docs
mkdir -p logs

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "⚠️ No .env file found. Please copy .env.example to .env and configure your secrets"
    cp .env.example .env
    echo "📝 Created .env file from template"
    echo ""
    echo "🔑 Please edit .env and add your API keys:"
    echo "   - OPENAI_API_KEY"
    echo "   - GITHUB_TOKEN"
    echo "   - GITHUB_REPO"
    echo "   - SLACK_BOT_TOKEN"
    echo "   - SLACK_APP_TOKEN"
    echo ""
else
    echo "✅ .env file already exists"
fi

echo ""
echo "🎉 Environment setup complete!"
echo ""
echo "Next steps:"
echo "1. Configure your .env file with API keys"
echo "2. Run: source .venv/bin/activate"
echo "3. Start GitTalker: python -m src.main"
echo ""