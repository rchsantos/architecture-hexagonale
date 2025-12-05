from typing import List
from fastapi import APIRouter
from fastapi.params import Depends

from app.application.dto import ProductCreateDTO
from app.application.use_cases import ProductService
from app.domain.models import Product
from app.presentation.api.dependencies import get_product_service

router = APIRouter(prefix="/products", tags=["products"])


@router.get(
    "/",
    response_model=List[Product],
    status_code=200,
    response_description="OK",
    summary="List all products",
    name="products",
    description="List all products",
)
def list_all_products(service: ProductService = Depends(get_product_service)):
    return service.list_products()


@router.post(
    "/",
    response_model=Product,
    status_code=201,
    response_description="Created",
    summary="Create a product",
    name="products",
    description="Create a product",
)
def create_product(
    payload: ProductCreateDTO,
    service: ProductService = Depends(get_product_service),
):
    return service.create_product(
        name=payload.name,
        price=payload.price,
    )