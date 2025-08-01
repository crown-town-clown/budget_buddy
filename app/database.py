#holds database engine, handles session
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os

#load environment variables
load_dotenv()
database_url = os.getenv("DATABASE_URL")

#create database engine
engine = create_engine(f"{database_url}")

#with Session(engine) as session: