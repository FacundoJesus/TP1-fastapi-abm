from pydantic import BaseModel,model_validator
from typing import List

# Entity
class Product(BaseModel):
    id: int
    code: str
    name: str
    description: str | None = None
    quantity: int
    in_stock: bool=True

    @model_validator(mode='after')
    def calculate_stock(self):
        # Si la cantidad es 0 o menor, in_stock pasa a False automáticamente
        if self.quantity < 1:
            self.in_stock = False
        else:
            self.in_stock = True
            
        return self




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