.PHONY: up down build test lint clean help

# Variables
DOCKER_COMPOSE = docker compose
FRONTEND_DIR = frontend
BACKEND_DIR = backend

# Colors for help messages
BLUE := \033[0;34m
NC := \033[0m # No Color

help: ## Display this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  ${BLUE}%-15s${NC} %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# Docker commands
up: ## Start all services
	$(DOCKER_COMPOSE) up

up-d: ## Start all services in detached mode
	$(DOCKER_COMPOSE) up -d

down: ## Stop all services
	$(DOCKER_COMPOSE) down

build: ## Build all services
	$(DOCKER_COMPOSE) build

rebuild: ## Rebuild all services
	$(DOCKER_COMPOSE) build --no-cache

# Frontend commands
frontend-install: ## Install frontend dependencies
	cd $(FRONTEND_DIR) && npm install

frontend-dev: ## Start frontend development server
	cd $(FRONTEND_DIR) && npm run dev

frontend-test: ## Run frontend tests
	cd $(FRONTEND_DIR) && npm test

frontend-lint: ## Run frontend linter
	cd $(FRONTEND_DIR) && npm run lint

# Backend commands
backend-install: ## Install backend dependencies
	cd $(BACKEND_DIR) && pip install -r requirements.txt

backend-migrate: ## Run backend migrations
	cd $(BACKEND_DIR) && python manage.py migrate

backend-test: ## Run backend tests
	cd $(BACKEND_DIR) && pytest

backend-lint: ## Run backend linter
	cd $(BACKEND_DIR) && flake8 .

# Development setup
setup: frontend-install backend-install ## Install all dependencies

# Testing
test: frontend-test backend-test ## Run all tests

# Linting
lint: frontend-lint backend-lint ## Run all linters

# Cleanup
clean: down ## Stop services and remove containers
	$(DOCKER_COMPOSE) down -v
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name "*.egg-info" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	find . -type d -name "node_modules" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg" -exec rm -r {} +
	find . -type d -name ".coverage" -exec rm -r {} +
	find . -type d -name "htmlcov" -exec rm -r {} +
	find . -type d -name ".mypy_cache" -exec rm -r {} +
	find . -type d -name ".ruff_cache" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	find . -type d -name ".tox" -exec rm -r {} +
	find . -type d -name "dist" -exec rm -r {} +
	find . -type d -name "build" -exec rm -r {} +

# Development workflow
dev: up-d ## Start development environment
	@echo "Development environment started. Access:"
	@echo "Frontend: http://localhost:5173"
	@echo "Backend: http://localhost:8000"

# Default target
.DEFAULT_GOAL := help
