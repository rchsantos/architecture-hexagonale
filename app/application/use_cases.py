from typing import List

from app.application.ports import ProductRepository
from app.domain.exceptions import ProductNotFound
from app.domain.models import Product


class ProductService:
    """
    Cas d'utilisation / Service applicatif.
    Il orchestre le domaine et dépend uniquement d'un port,
    jamais d'une implémentation concrète.
    """
    def __init__(self, repository: ProductRepository):
        self._repository = repository


    def list_products(self) -> List[Product]:
        return self._repository.get_all()


    def get_product(self, product_id: str) -> Product:
        product = self._repository.get_by_id(product_id)
        if product is None:
            raise ProductNotFound(product_id)
        return product


    def create_product(self, name: str, price: float) -> Product:
        product = Product(name=name, price=price)
        self._repository.save(product)
        return product
