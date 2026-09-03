from fastapi import APIRouter, HTTPException, status
from models.product import Product, ProductCreate, GetProductByIdResponse, GetProductsResponse, CreateProductResponse, DeleteProductResponse, UpdateProductResponse

router = APIRouter()

# Array de Productos
products = []
current_id = 0  # Contador global
# Obtener todos los productos
@router.get("/products", status_code=status.HTTP_200_OK)
def get_all_products() -> GetProductsResponse:
    return GetProductsResponse(products=products)

    
# Obtener los productos en Stock
@router.get("/products/instock", status_code=status.HTTP_200_OK)
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
@router.get("/products/outstock", status_code=status.HTTP_200_OK)
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
@router.post("/products", status_code=status.HTTP_201_CREATED)
def add_product(new_product: ProductCreate) -> CreateProductResponse:  # <-- Recibe ProductCreate

    # 1. Validar que no exista otro producto con el mismo código
    for existProduct in products:
        if existProduct.code == new_product.code:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Product with CODE {new_product.code} already exists"
            )

    # 2. Generamos el ID sumando 1 al contador
    current_id += 1
    next_id = current_id

    # 3. Crear la entidad completa Product
    product_to_save = Product(
        id=next_id,
        code=new_product.code,
        name=new_product.name,
        description=new_product.description,
        quantity=new_product.quantity,
        in_stock=new_product.quantity > 0
    )

    # 4. Guardar en memoria
    products.append(product_to_save)

    # 5. Retornar la respuesta con el producto completo (ya con ID y stock)
    return CreateProductResponse(
        message="Product created successfully",
        product=product_to_save
    )

# Eliminar Producto por ID
@router.delete("/product/{id}", status_code=status.HTTP_200_OK)
def delete_product(idProduct: int) -> DeleteProductResponse:

    for product in products:
        if product.id == idProduct:
            products.remove(product)
            return DeleteProductResponse(message="Product deleted succesfully")

    raise HTTPException (
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Product not found"
    )


# Actualizar Producto
@router.put("/products/{id}", status_code=status.HTTP_200_OK)
def update_product(id: int, updated_data: ProductCreate) -> UpdateProductResponse:

    for index, existing_product in enumerate(products):
        if existing_product.id == id:

            # 1. Validar que el nuevo 'code' no lo tenga OTRO producto distinto
            for product in products:
                if product.code == updated_data.code and product.id != id:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"Product with CODE {updated_data.code} already exists"
                    )

            # 2. Armar el producto actualizado manteniendo el ID de la URL
            product_updated = Product(
                id=id,
                code=updated_data.code,
                name=updated_data.name,
                description=updated_data.description,
                quantity=updated_data.quantity,
                in_stock=updated_data.quantity > 0
            )

            # 3. Reemplazar en la lista
            products[index] = product_updated

            return UpdateProductResponse(
                message="Product updated successfully",
                product=product_updated
            )
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product with ID: {id} not found"
    )


# Buscar y Obtener Producto por ID
@router.get("/products/{id}", status_code=status.HTTP_200_OK)
def get_product_by_id(id:int) -> GetProductByIdResponse:

    for product in products:
        if product.id == id:
            return GetProductByIdResponse(product=product)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product with ID: {id} not found"
    )