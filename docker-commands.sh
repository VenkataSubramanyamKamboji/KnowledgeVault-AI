#!/bin/bash
# KnowledgeVault AI - Docker Quick Commands
# Usage: chmod +x docker-commands.sh && ./docker-commands.sh [command]

COMPOSE_FILE="docker-compose.yml"
DEV_COMPOSE_FILE="docker-compose.dev.yml"

case "${1:-help}" in
  build)
    echo "Building production Docker image..."
    docker build -t knowledgevault-ai:latest .
    ;;
  build-dev)
    echo "Building development Docker image..."
    docker-compose -f $DEV_COMPOSE_FILE build
    ;;
  start)
    echo "Starting application with Docker Compose..."
    docker-compose up -d
    echo "✓ Application started"
    echo "  Web UI: http://localhost:8000"
    echo "  API Docs: http://localhost:8000/docs"
    ;;
  dev)
    echo "Starting development environment with hot-reload..."
    docker-compose -f $DEV_COMPOSE_FILE up
    ;;
  stop)
    echo "Stopping application..."
    docker-compose down
    echo "✓ Application stopped"
    ;;
  restart)
    echo "Restarting application..."
    docker-compose restart
    echo "✓ Application restarted"
    ;;
  logs)
    echo "Showing application logs..."
    docker-compose logs -f
    ;;
  shell)
    echo "Opening container shell..."
    docker exec -it knowledgevault bash
    ;;
  health)
    echo "Checking application health..."
    curl -s http://localhost:8000/health | jq . || echo "Application not responding"
    ;;
  clean)
    echo "Removing containers and volumes..."
    docker-compose down -v
    echo "✓ Cleanup complete"
    ;;
  prune)
    echo "Removing unused Docker resources..."
    docker system prune -a --volumes -f
    echo "✓ Prune complete"
    ;;
  status)
    echo "Checking container status..."
    docker-compose ps
    ;;
  rebuild)
    echo "Rebuilding and restarting..."
    docker-compose down
    docker-compose up --build -d
    echo "✓ Application rebuilt and started"
    ;;
  *)
    echo "KnowledgeVault AI - Docker Commands"
    echo ""
    echo "Usage: ./docker-commands.sh [command]"
    echo ""
    echo "Commands:"
    echo "  build          Build production Docker image"
    echo "  build-dev      Build development Docker image"
    echo "  start          Start application with Docker Compose"
    echo "  dev            Start development environment with hot-reload"
    echo "  stop           Stop application"
    echo "  restart        Restart application"
    echo "  logs           Show application logs"
    echo "  shell          Open container shell"
    echo "  health         Check application health"
    echo "  status         Show container status"
    echo "  clean          Remove containers and volumes"
    echo "  prune          Remove unused Docker resources"
    echo "  rebuild        Rebuild and restart application"
    echo ""
    echo "Examples:"
    echo "  ./docker-commands.sh start"
    echo "  ./docker-commands.sh dev"
    echo "  ./docker-commands.sh logs"
    echo "  ./docker-commands.sh shell"
    ;;
esac
