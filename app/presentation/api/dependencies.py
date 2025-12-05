from fastapi import Depends

from app.application.ports import ProductRepository
from app.application.use_cases import ProductService
from app.infrastructure.adapters.in_memory.in_memory_product_repository import InMemoryProductRepository


def get_repository() -> ProductRepository:
    """
    Ici on utilise l'adaptateur en mémoire.
    :return:
    """
    return InMemoryProductRepository()


def get_product_service(
        repo: ProductRepository = Depends(get_repository),
) -> ProductService:
    return ProductService(repository=repo)