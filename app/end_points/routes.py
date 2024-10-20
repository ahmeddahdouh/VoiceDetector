from fastapi import APIRouter, Depends ,HTTPException
from sqlalchemy.orm import Session

from app.core.config import db_dependency, get_db
from app.core.security import verify_jwt
from app.schema.shema import UserBase, UserCreate, UserResponse
from app.services import user_service
from app.services.user_service import register_user, authenticate_user

router = APIRouter()


@router.get("/allusers/")
async def get_users(db: db_dependency, token: str = Depends(verify_jwt)):
    return user_service.get_users(db)


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user)


@router.post("/login")
async def login(username: str, password: str, db: db_dependency):
    user = authenticate_user(db, username, password)

    if user is None:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    # Si l'utilisateur est authentifié, vous pouvez retourner des informations sur l'utilisateur ou un jeton
    return {"message": "Login successful", "user": user}