# Production Makefile for GitTalker

.PHONY: help install test lint clean dev build deploy

# Default target
help:
	@echo "GitTalker Production Commands:"
	@echo ""
	@echo "Setup & Development:"
	@echo "  make install    - Set up development environment"
	@echo "  make dev        - Start development server"
	@echo "  make test       - Run tests"
	@echo "  make lint       - Run code quality checks"
	@echo ""
	@echo "Production:"
	@echo "  make build      - Build Docker container"
	@echo "  make deploy     - Deploy to production"
	@echo "  make clean      - Clean up temporary files"

# Development setup
install:
	@echo "🚀 Setting up GitTalker development environment..."
	./setup_env.sh

# Start development server
dev:
	@echo "🔥 Starting GitTalker in development mode..."
	source .venv/bin/activate && python -m src.main

# Run tests
test:
	@echo "🧪 Running GitTalker tests..."
	source .venv/bin/activate && python test_personality.py

# Code quality checks
lint:
	@echo "🔍 Running code quality checks..."
	source .venv/bin/activate && \
	python -m ruff check src/ && \
	python -m mypy src/ --ignore-missing-imports

# Build Docker container
build:
	@echo "🐳 Building GitTalker Docker container..."
	docker build -t gittalker:latest .

# Deploy to production
deploy:
	@echo "🚀 Deploying GitTalker to production..."
	docker-compose up -d

# Clean up
clean:
	@echo "🧹 Cleaning up..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf docs/.docs_cache.json docs/.embeddings_cache.npz docs/.metadata_cache.json
	docker system prune -f

# Quick development cycle
quick: clean lint test
	@echo "✅ Quick development check complete!"