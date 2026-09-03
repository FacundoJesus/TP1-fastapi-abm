from fastapi import APIRouter, HTTPException, status
from models.product import Product, GetProductsResponse, CreateProductResponse, DeleteProductResponse, UpdateProductResponse

router = APIRouter()

# Array de Productos
products = []

# Obtener todos los productos
@router.get("/products")
def get_all_products() -> GetProductsResponse:
    return GetProductsResponse(products=products)

    
# Obtener los productos en Stock
@router.get("/products/instock")
def get_in_stock_products() -> GetProductsResponse:
    inStock = []

    for product in products:
        if product.in_stock == True:
            inStock.append(product)

    if not inStock:
        raise HTTPException (
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "There are no products in stock"
        )

    return GetProductsResponse(products=inStock)


# Obtener los productos sin Stock
@router.get("/products/outstock")
def get_out_stock_products() -> GetProductsResponse:

    outStock= []

    for product in products:
        if product.in_stock == False:
            outStock.append(product)

    if not outStock:
        raise HTTPException (
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "There are no out of stock products"
        )

    
# Agregar Producto
@router.post("/products")
def add_product(newProduct:Product) -> CreateProductResponse:

    for existProduct in products:
        if existProduct.id == newProduct.id:
            raise HTTPException (
            status_code = status.HTTP_400_BAD_REQUEST,
            detail= f"Product with ID {newProduct.id} already exists"
            )
        if existProduct.code == newProduct.code:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Product with CODE {newProduct.code} already exists"
            )

    products.append(newProduct)

    return CreateProductResponse(
        message="Product created successfully",
        product= newProduct
    )

# Eliminar Producto

# Actualizar Producto

# Buscar Producto por ID