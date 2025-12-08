import pytest
from django.test import TestCase

from app.domain.models import Product
from app.infrastructure.adapters.django_orm.product_repository import DjangoProductRepository


class TestDjangoProductRepository(TestCase):
    def setUp(self):
        self.repository = DjangoProductRepository()


    def test_save_and_get_by_id(self):
        product = Product(name="Test Product", price=100)

        # save and found product
        self.repository.save(product)
        product_loaded = self.repository.get_by_id(product.id)

        # assert
        self.assertIsNotNone(product_loaded)
        self.assertEqual(product_loaded.id, product.id)
        self.assertEqual(product_loaded.name, product.name)
        self.assertEqual(product_loaded.price, product.price)


    def test_get_all_returns_all_products(self):
        product_1 = Product(name="Test Product", price=100)
        product_2 = Product(name="Test Product2", price=15.0)

        self.repository.save(product_1)
        self.repository.save(product_2)

        products = self.repository.get_all()

        self.assertEqual(len(products), 2)
        ids = {p.id for p in products}
        self.assertIn(product_1.id, ids)
        self.assertIn(product_2.id, ids)


    def test_get_by_id_returns_none_if_not_found(self):
        result = self.repository.get_by_id("unknows-id")
        self.assertIsNone(result)
