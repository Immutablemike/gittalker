#!/usr/bin/env python3
"""
Quick test script for GitTalker personality and scope enforcement
"""
import asyncio
import os
import sys

# Add src to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.agent import GitTalkerAgent

async def test_agent_personality():
    """Test GitTalker agent responses and personality."""
    agent = GitTalkerAgent()
    
    print("� GitTalker Urban Personality Test")
    print("=" * 50)
    
    # Test cases with urban context
    test_cases = [
        {
            "name": "In-scope query with context",
            "query": "How do I install the dependencies?",
            "context": "# Installation\nRun `pip install -r requirements.txt` to install all dependencies. This sets up the entire build environment."
        },
        {
            "name": "Out-of-scope query (weather)",
            "query": "What's the weather like today?",
            "context": ""
        },
        {
            "name": "No context available",
            "query": "How do I setup the database configuration?",
            "context": ""
        },
        {
            "name": "Urban query style",
            "query": "Yo, how do I get this build running?",
            "context": "# Build Process\nTo start the build: `npm run build`\nFor development: `npm run dev`"
        }
    ]
    
    for test in test_cases:
        print(f"\n📋 Test: {test['name']}")
        print(f"Query: {test['query']}")
        
        # Test query validation
        is_valid = agent.is_valid_query(test['query'])
        print(f"Valid query: {is_valid}")
        
        if is_valid:
            # Test response generation
            response = await agent.generate_response(test['query'], test['context'])
            print(f"Response: {response}")
        else:
            print("❌ Query rejected by validation")
        
        print("-" * 30)
    
    # Show personality info
    print("\n🤖 Agent Personality Info:")
    personality = agent.get_personality_info()
    for key, value in personality.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    # Set dummy environment variables for testing
    os.environ.setdefault("OPENAI_API_KEY", "test-key")
    os.environ.setdefault("GITHUB_TOKEN", "test-token")
    os.environ.setdefault("GITHUB_REPO", "test/repo")
    os.environ.setdefault("SLACK_BOT_TOKEN", "test-slack-token")
    os.environ.setdefault("SLACK_APP_TOKEN", "test-app-token")
    
    asyncio.run(test_agent_personality())