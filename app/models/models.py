from sqlalchemy import Integer, String, Column, ForeignKey, Float, ARRAY

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String, nullable=False)
    vocal_data = Column(ARRAY(Float), nullable=True)
