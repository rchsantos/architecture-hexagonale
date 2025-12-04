from abc import ABC, abstractmethod
from typing import Optional
from app.domain.models import Product


class ProductRepository(ABC):
    """
    Port secondaire : Interface définie par le domaine/application.
    """


    @abstractmethod
    def get_by_id(self, product_id: str) -> Optional[Product]:
        raise NotImplementedError()


    @abstractmethod
    def save(self, product: Product) -> None:
        raise NotImplementedError()


    @abstractmethod
    def get_all(self) -> list[Product]:
        raise NotImplementedError()