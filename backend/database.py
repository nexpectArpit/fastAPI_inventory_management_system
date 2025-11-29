#Ye database connection handle karta hai
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url="postgresql://arpittripathi@localhost:5432/arpittripathi"

#Engine ke through SQLAlchemy SQL queries bhejta hai, results leta hai, aur sessions create karta hai.
engine=create_engine(db_url)

#Flush memory data ko SQL statements me convert karta hai, par database me commit nahi karta.
session=sessionmaker(autocommit=False,autoflush=False,bind=engine)
