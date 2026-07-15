from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.auth import router as auth_router

from app.database.database import Base, engine
from app.models.user import User
from app.models.knowledge import KnowledgeItem
from app.routers.knowledge import router as knowledge_router

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="KnowledgeVault AI",
    version="1.0.0"
)
app.include_router(auth_router)
app.include_router(knowledge_router)

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "KnowledgeVault AI Backend Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "version": "1.0.0"
    }