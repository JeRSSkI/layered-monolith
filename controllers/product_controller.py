from fastapi import APIRouter, HTTPException
from app.application.use_cases.create_product import CreateProduct
from app.application.use_cases.list_products import ListProducts

router = APIRouter()

def setup_product_routes(router, repository):
    create_uc = CreateProduct(repository)
    list_uc = ListProducts(repository)

    @router.get("/products")
    async def list_products():
        return await list_uc.execute()

    @router.post("/products", status_code=201)
    async def create_product(dto: dict):
        try:
            return await create_uc.execute(dto)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
