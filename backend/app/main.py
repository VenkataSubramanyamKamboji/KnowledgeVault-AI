import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routers.auth import router as auth_router

from app.database.database import Base, engine
from app.models.user import User
from app.models.knowledge import KnowledgeItem
from app.routers.knowledge import router as knowledge_router
from app.routers.search import router as search_router
from app.routers.chat import router as chat_router

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="KnowledgeVault AI",
    version="1.0.0"
)

# Include API routers
app.include_router(auth_router)
app.include_router(knowledge_router)
app.include_router(search_router)
app.include_router(chat_router)

# CORS configuration
origins = [
    "http://localhost:5173",
    "http://localhost:8000",
    "http://localhost",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (frontend build)
static_dir = Path(__file__).parent / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=static_dir), name="static")
    
    @app.get("/", include_in_schema=False)
    async def serve_index():
        """Serve the frontend index.html"""
        index_file = static_dir / "index.html"
        if index_file.exists():
            return FileResponse(index_file)
        return {"message": "KnowledgeVault AI Backend Running"}
else:
    @app.get("/")
    def root():
        return {
            "message": "KnowledgeVault AI Backend Running",
            "note": "Frontend not built. Run 'npm run build' in frontend directory."
        }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "version": "1.0.0"
    }