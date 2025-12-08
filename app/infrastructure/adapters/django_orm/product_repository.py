from typing import Optional

from django.core.exceptions import ValidationError

from app.application.ports import ProductRepository
from app.domain.models import Product
from app.infrastructure.adapters.django_orm.product_mapper import ProductMapper
from app.infrastructure.adapters.django_orm.product_model import ProductModel


class DjangoProductRepository(ProductRepository):

    def save(self, product: Product):
        """
        Saves a product into the database.
        :param product: Product
        :return: None
        """
        data = ProductMapper.to_orm(product)
        ProductModel.objects.update_or_create(
            id=data["id"],
            defaults=data
        )


    def get_by_id(self, product_id: str) -> Optional[Product]:
        """
        Gets a product by id from the database.
        :param product_id: product id
        :return: Product or None
        """
        try:
            model = ProductModel.objects.get(id=product_id)
        except (ProductModel.DoesNotExist, ValidationError):
            return None
        return ProductMapper.to_domain(model)


    def get_all(self) -> list[Product]:
        """
        Gets all products from the database.
        :return:  list[Product]
        """
        return [
            ProductMapper.to_domain(model)
            for model in ProductModel.objects.all()
        ]