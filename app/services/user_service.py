# app/user_service.py
from datetime import timedelta
from fastapi import FastAPI, HTTPException
from sqlmodel import Session
from app.core.security import (
    verify_password,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    create_access_token,
)
from app.repositories.user_repository import (
    get_user_by_email,
    get_user_by_username,
    get_all_users,
    create_user,
)
from app.schema.shema import UserCreate


def register_user(db: Session, user: UserCreate):
    # Vérification de l'existence de l'utilisateur par email
    existing_user_email = get_user_by_email(db, user.email)
    if existing_user_email:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Vérification de l'existence de l'utilisateur par nom d'utilisateur
    existing_user_username = get_user_by_username(db, user.username)
    if existing_user_username:
        raise HTTPException(status_code=400, detail="Username already taken")
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
