from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user import UserCreate, UserLogin
from app.services.auth_service import create_user, authenticate_user
from app.core.jwt_handler import create_access_token

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    created_user = create_user(db, user)

    if created_user is None:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    return {
        "message": "User registered successfully",
        "user_id": created_user.id
    }

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    authenticated_user = authenticate_user(
        db,
        user.email,
        user.password
    )

    if authenticated_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    #In JWT (JSON Web Token), sub is a standard claim defined by the JWT specification.
    access_token = create_access_token(
        {
            "sub": authenticated_user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }