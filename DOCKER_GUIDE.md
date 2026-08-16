# KnowledgeVault AI - Docker Setup Guide

## Overview
This guide covers building and running the KnowledgeVault AI application using Docker.

### Architecture
- **Frontend**: React + Vite (built to static files during Docker build)
- **Backend**: FastAPI + Python
- **Database**: SQLite (persisted via Docker volume)
- **Vector Store**: Chroma DB (persisted via Docker volume)

## Quick Start

### Option 1: Using Docker Compose (Recommended)

1. **Build and start the application:**
   ```bash
   docker-compose up --build
   ```

2. **Access the application:**
   - Web UI: http://localhost:8000
   - API Docs: http://localhost:8000/docs
   - Health Check: http://localhost:8000/health

3. **Stop the application:**
   ```bash
   docker-compose down
   ```

### Option 2: Build Docker Image Manually

1. **Build the image:**
   ```bash
   docker build -t knowledgevault-ai:latest .
   ```

2. **Run the container:**
   ```bash
   docker run -d \
     --name knowledgevault \
     -p 8000:8000 \
     -v knowledgevault-db:/app/chroma_db \
     -v knowledgevault-db:/app/knowledgevault.db \
     knowledgevault-ai:latest
   ```

3. **Access the application:**
   - http://localhost:8000

4. **Stop the container:**
   ```bash
   docker stop knowledgevault
   docker rm knowledgevault
   ```

## Docker Commands

### View logs:
```bash
docker-compose logs -f
# or manually
docker logs -f knowledgevault
```

### Check container status:
```bash
docker-compose ps
# or manually
docker ps
```

### Access container shell:
```bash
docker exec -it knowledgevault bash
```

### Remove all data and rebuild:
```bash
docker-compose down -v
docker-compose up --build
```

## Environment Variables

Create a `.env` file in the root directory to override defaults:

```env
PYTHONUNBUFFERED=1
APP_ENV=production
```

Or use the provided `.env.docker` file:
```bash
docker-compose --env-file .env.docker up --build
```

## Dockerfile Details

The Dockerfile uses a **multi-stage build** to optimize image size:

1. **Stage 1 (frontend-builder)**: Node.js image builds the React frontend
   - Installs dependencies from `frontend/package.json`
   - Runs `npm run build` to create production-ready static files

2. **Stage 2 (backend)**: Python 3.11 slim image
   - Installs Python dependencies from `backend/requirements.txt`
   - Copies the built frontend to `/app/static`
   - Runs FastAPI/Uvicorn server

This approach keeps the final image lean while packaging everything needed.

## Persistent Volumes

Data is persisted through Docker volumes:
- `knowledgevault-db`: Stores SQLite database and Chroma DB data
- Mount point: `/app/chroma_db` and `/app/knowledgevault.db`

## Production Deployment

For production, consider:

1. **Update CORS origins** in `.env.docker` or `backend/app/main.py`
2. **Use environment variables** for sensitive configuration
3. **Add reverse proxy** (Nginx) in front of the application
4. **Enable HTTPS** with SSL certificates
5. **Scale with multiple replicas** using Docker Swarm or Kubernetes

Example with Nginx:
```yaml
# Add to docker-compose.yml
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - knowledgevault
```

## Troubleshooting

### Port already in use:
```bash
# Change port in docker-compose.yml
# Change: ports: - "8000:8000"
# To:     ports: - "8001:8000"
```

### Database not persisting:
- Ensure volumes are properly mounted
- Check Docker Desktop/Engine volumes: `docker volume ls`
- Verify volume permissions

### Frontend not loading:
- Verify build succeeded: `docker logs knowledgevault`
- Check static files exist in container: `docker exec knowledgevault ls -la /app/static`
- Ensure CORS is properly configured

### API endpoints not responding:
- Check backend logs: `docker logs knowledgevault`
- Verify all dependencies installed: Check `backend/requirements.txt`
- Test health endpoint: `curl http://localhost:8000/health`

## Building for Different Platforms

Build for ARM64 (Apple Silicon, some servers):
```bash
docker buildx build --platform linux/arm64,linux/amd64 -t knowledgevault-ai:latest .
```

## Cleaning Up

Remove unused Docker resources:
```bash
docker system prune -a
```

This removes:
- Stopped containers
- Unused images
- Unused networks
- Build cache

## Next Steps

1. Configure environment variables for your deployment
2. Update CORS origins for your domain
3. Set up proper logging and monitoring
4. Consider adding a reverse proxy (Nginx) for production
5. Implement SSL/TLS certificates
