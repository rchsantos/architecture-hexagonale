from typing import Iterable

from app.domain.models import Product


def calculate_total_value(products: Iterable[Product]) -> float:
    """
    Exemple de petit service de domaine.
    :param products:
    :return:
    """
    return sum(product.value for product in products)