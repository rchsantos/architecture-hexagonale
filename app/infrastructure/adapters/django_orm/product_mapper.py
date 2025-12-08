from app.domain.models import Product


class ProductMapper:


    @staticmethod
    def to_domain(model) -> Product:
        return Product(
            id=str(model.id),
            name=model.name,
            price=model.price,
        )


    @staticmethod
    def to_orm(product: Product) -> dict:
        return {
            "id": product.id,
            "name": product.name,
            "price": product.price,
        }