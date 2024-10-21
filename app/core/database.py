from fastapi import Depends
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.annotation import Annotated

DATABASE_URL = "postgresql://postgres:admin@localhost:5432/dorianDatabase"

engine = create_engine(DATABASE_URL)

Base = declarative_base()




