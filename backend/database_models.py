#isme SQLAlchemy ORM tables honge.Yahi file table structure define karti hai.Database me rows isi file ke hisaab se save hote hain
from sqlalchemy import Column,Integer,String,Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

#Ye SQLAlchemy ko batata hai ki: ab hum ORM table models banayenge
Base=declarative_base()

#Is Base ko use karke SQLAlchemy real tables banata hai
class Product(Base): #BaseModel gives you structured data validation.
    __tablename__="product"
    id= Column(Integer,primary_key=True,index=True)
    name=Column(String)
    description=Column(String)
    price=Column(Float)
    quantity=Column(Integer)

