# app/router.py
from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session
from app.core.database import engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]