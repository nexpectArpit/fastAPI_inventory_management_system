#Ye database connection handle karta hai
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os


base = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(base, ".env"))

db_url=os.getenv("DATABASE_URL")
print("DB URL:", db_url)#just for check

#Engine ke through SQLAlchemy SQL queries bhejta hai, results leta hai, aur sessions create karta hai.
engine=create_engine(db_url)

#Flush memory data ko SQL statements me convert karta hai, par database me commit nahi karta.
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()