from fastapi import Depends,FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.models import Product
from backend.database import SessionLocal, engine, get_db
import backend.database_models as database_models
from sqlalchemy.orm import Session


app=FastAPI()

#to hnadle the cors error
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#contains all your SQLAlchemy ORM classes
#below line will create the table for us
database_models.Base.metadata.create_all(bind=engine)

# health check
@app.get("/") # @ is decorator?means
def greet():
    return "welcome to arpit trac"

#  dummy data if, db not worked
products=[
    Product(id=1,name="phone",description="budget phone",price=99,quantity=10),
    Product(id=2,name="laptop",description="game laptop",price=999,quantity=10),
    Product(id=3,name="pen",description="ball pen",price=3,quantity=30),
    Product(id=5,name="table",description="wooden",price=700,quantity=800)
]

def init_db():#fn. to add data in db
    db=SessionLocal()
    count=db.query(database_models.Product).count()
    if (count==0):
        for product in products:
        #converting a Pydantic model into a SQLAlchemy model and saving it in the database.
        #here we doing unpacking it
            db.add(database_models.Product(**product.model_dump()))
        # product.model_dump()->Ye Pydantic object ko Python dictionary mein convert karta hai
        #database_models.Product(...)->Ye SQLAlchemy ORM model ka constructor hai
        # ** ->give key value pair of dictionary

        db.commit()


    # db.query()

init_db()

@app.get("/products")
def get_all_products(db:Session=Depends(get_db)):#here we injecting the dependency
    # #db connection
    # db=session()
    # #query
    # db.query()
    db_products=db.query(database_models.Product).all()
    return db_products

#db:Session=Depends(get_db) <- this is dependency injection

@app.get("/products/{id}")
def get_product_by_id(id:int,db:Session=Depends(get_db)):
    # for product in products:
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
            return db_product
    return "product not found"


@app.post("/products")
def add_product(product:Product,db:Session = Depends(get_db)):
    exists=db.query(database_models.Product).filter(database_models.Product.id==product.id).first()
    if exists:
        return "ID alredy existes"
    new_product=database_models.Product(**product.model_dump())
    db.add(new_product)
    db.commit()#after adding ,we have to commit the changes also na
    db.refresh(new_product)
    return new_product

@app.put("/products/{id}")

def update_product(id:int,product:Product,db:Session= Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:#if product exist
        #update the details
        db_product.name=product.name
        db_product.description=product.description
        db_product.price=product.price
        db_product.quantity=product.quantity
        db.commit()
        return "Product updated "
    else:
        return "No product found"

    # for i in range(len(products)):
    #     if(products[i].id==id):
    #         products[i]=product
    #         return "product added successfully"


@app.delete("/products/{id}")
def delete_product(id:int,db:Session= Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if (db_product):
        db.delete(db_product)
        db.commit()
        return "product deleted successfully"

    else:
        return "product not found"



    # for i in range(len(products)):
    #     if(products[i].id==id):
    #         del products[i]
    #         return "product deleted successfully"
    # if product not found

