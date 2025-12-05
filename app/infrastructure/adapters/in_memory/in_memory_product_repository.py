from typing import Dict, Optional, List

from app.application.ports import ProductRepository
from app.domain.models import Product


class InMemoryProductRepository(ProductRepository):
    """
    Adaptateur secondaire.
    Implémentation simple en mémoire pour les tests ou démos.
    """
    def __init__(self):
        self._data: Dict[str, Product] = {}


    def get_by_id(self, product_id: str) -> Optional[Product]:
        return self._data.get(product_id)


    def save(self, product: Product) -> None:
        self._data[product.id] = product


    def get_all(self) -> List[Product]:
        return list(self._data.values())