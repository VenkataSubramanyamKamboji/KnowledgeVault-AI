# KnowledgeVault AI - Docker Quick Commands (PowerShell)
# Usage: .\docker-commands.ps1 [command]

param(
    [string]$Command = "help"
)

$DevComposeFile = "docker-compose.dev.yml"

switch ($Command.ToLower()) {
    "build" {
        Write-Host "Building production Docker image..." -ForegroundColor Cyan
        docker build -t knowledgevault-ai:latest .
    }
    "build-dev" {
        Write-Host "Building development Docker image..." -ForegroundColor Cyan
        docker-compose -f $DevComposeFile build
    }
    "start" {
        Write-Host "Starting application with Docker Compose..." -ForegroundColor Cyan
        docker-compose up -d
        Write-Host "✓ Application started" -ForegroundColor Green
        Write-Host "  Web UI: http://localhost:8000" -ForegroundColor White
        Write-Host "  API Docs: http://localhost:8000/docs" -ForegroundColor White
    }
    "dev" {
        Write-Host "Starting development environment with hot-reload..." -ForegroundColor Cyan
        docker-compose -f $DevComposeFile up
    }
    "stop" {
        Write-Host "Stopping application..." -ForegroundColor Cyan
        docker-compose down
        Write-Host "✓ Application stopped" -ForegroundColor Green
    }
    "restart" {
        Write-Host "Restarting application..." -ForegroundColor Cyan
        docker-compose restart
        Write-Host "✓ Application restarted" -ForegroundColor Green
    }
    "logs" {
        Write-Host "Showing application logs..." -ForegroundColor Cyan
        docker-compose logs -f
    }
    "shell" {
        Write-Host "Opening container shell..." -ForegroundColor Cyan
        docker exec -it knowledgevault bash
    }
    "health" {
        Write-Host "Checking application health..." -ForegroundColor Cyan
        try {
            $response = Invoke-WebRequest -Uri "http://localhost:8000/health" -UseBasicParsing -ErrorAction Stop
            Write-Host $response.Content -ForegroundColor Green
        }
        catch {
            Write-Host "Application not responding" -ForegroundColor Red
        }
    }
    "clean" {
        Write-Host "Removing containers and volumes..." -ForegroundColor Cyan
        docker-compose down -v
        Write-Host "✓ Cleanup complete" -ForegroundColor Green
    }
    "prune" {
        Write-Host "Removing unused Docker resources..." -ForegroundColor Cyan
        docker system prune -a --volumes -f
        Write-Host "✓ Prune complete" -ForegroundColor Green
    }
    "status" {
        Write-Host "Checking container status..." -ForegroundColor Cyan
        docker-compose ps
    }
    "rebuild" {
        Write-Host "Rebuilding and restarting..." -ForegroundColor Cyan
        docker-compose down
        docker-compose up --build -d
        Write-Host "✓ Application rebuilt and started" -ForegroundColor Green
    }
    default {
        Write-Host "KnowledgeVault AI - Docker Commands" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "Usage: .\docker-commands.ps1 [command]" -ForegroundColor White
        Write-Host ""
        Write-Host "Commands:" -ForegroundColor Yellow
        Write-Host "  build          Build production Docker image"
        Write-Host "  build-dev      Build development Docker image"
        Write-Host "  start          Start application with Docker Compose"
        Write-Host "  dev            Start development environment with hot-reload"
        Write-Host "  stop           Stop application"
        Write-Host "  restart        Restart application"
        Write-Host "  logs           Show application logs"
        Write-Host "  shell          Open container shell"
        Write-Host "  health         Check application health"
        Write-Host "  status         Show container status"
        Write-Host "  clean          Remove containers and volumes"
        Write-Host "  prune          Remove unused Docker resources"
        Write-Host "  rebuild        Rebuild and restart application"
        Write-Host ""
        Write-Host "Examples:" -ForegroundColor Yellow
        Write-Host "  .\docker-commands.ps1 start"
        Write-Host "  .\docker-commands.ps1 dev"
        Write-Host "  .\docker-commands.ps1 logs"
        Write-Host "  .\docker-commands.ps1 shell"
    }
}
