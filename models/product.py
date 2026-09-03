from pydantic import BaseModel
from typing import List

# Entity
class Product(BaseModel):
    id: int | None = None
    code: str
    name: str
    description: str | None = None
    quantity: int
    in_stock: bool=True


# Responses
class GetProductsResponse(BaseModel):
    products: List[Product]

class CreateProductResponse(BaseModel):
    message:str
    product:Product

class DeleteProductResponse(BaseModel):
    message:str

class UpdateProductResponse(BaseModel):
    message:str
    product:Product