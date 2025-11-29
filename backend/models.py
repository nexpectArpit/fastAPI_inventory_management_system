#Ye sirf Pydantic models ke liye hota hai,Sirf API validation deta hai

from pydantic import BaseModel


class Product(BaseModel): #BaseModel gives you structured data validation.
    id: int
    name: str
    description:str
    price: float
    quantity:int


    ##do not use constructor when we use pydantic
    # def __init__(self,id:int,name:str,description:str,price:float,quantity:int):8
    #     self.id=id
    #     self.name=name
    #     self.description=description
    #     self.price=price
    #     self.quantity=quantity


