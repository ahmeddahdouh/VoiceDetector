# app/user_service.py
from datetime import timedelta
from http.client import HTTPException

from sqlmodel import Session

import app
from app.core.security import verify_password, hash_password, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from app.models.models import User
from app.repositories.user_repository import get_user_by_email, get_user_by_username, get_all_users,create_user
from app.schema.shema import UserCreate


def register_user(db: Session, user: UserCreate):
    if get_user_by_email(db, user.email) or get_user_by_username(db, user.username):
        raise HTTPException(status_code=400, detail="User already registered")
    return create_user(db, user)

def get_users(db: Session):
    users = get_all_users(db)
    return users

def authenticate_user(db: Session, username: str, password: str):
    # Récupérer l'utilisateur depuis la base de données
    user = get_user_by_username(db, username)
    if not user or not verify_password(password, user.password):
        return None
    # Générer le token JWT si l'authentification réussit
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

