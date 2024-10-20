from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.models import User
from app.schema.shema import UserCreate


def get_all_users(db: Session):
    return db.query(User).all()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, email=user.email,
                   password= hash_password(user.password),
                   vocal_data=user.vocal_data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
