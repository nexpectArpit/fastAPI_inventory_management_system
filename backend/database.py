#Ye database connection handle karta hai
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# First check if DATABASE_URL is already set as environment variable (for production/Render)
# If not, load from .env file (for local development)
if not os.getenv("DATABASE_URL"):
    base = os.path.dirname(os.path.abspath(__file__))
    load_dotenv(os.path.join(base, ".env"))

db_url = os.getenv("DATABASE_URL")

# Handle postgres:// to postgresql:// conversion (some providers use postgres://)
if db_url and db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

if not db_url:
    raise ValueError("DATABASE_URL environment variable is not set")

print("DB URL:", db_url if not db_url or "@" not in db_url else db_url.split("@")[0] + "@***")  # Hide password in logs

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