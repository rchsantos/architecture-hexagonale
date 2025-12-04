
class DomainException(Exception):
    """Base class for domain-related exceptions."""


class ProductNotFound(DomainException):
    """Raised when a product cannot be found."""
    def __init__(self, product_id: str):
        super().__init__('Product with id "{}" not found'.format(product_id))
        self.product_id = product_id