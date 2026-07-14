from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password
from app.core.security import verify_password


def create_user(db: Session, user: UserCreate):
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        return None

    hashed_password = hash_password(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def authenticate_user(db: Session, email: str, password: str):
    # Find the user by email
    user = db.query(User).filter(User.email == email).first()

    # User not found
    if user is None:
        return None

    # Password is incorrect
    if not verify_password(password, user.password):
        return None

    # Authentication successful
    return user