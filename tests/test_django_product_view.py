import json

from django.test import TestCase, Client

from app.infrastructure.adapters.django_orm.product_model import ProductModel


class TestDjangoProductView(TestCase):
    def setUp(self):
        self.client = Client()


    def test_create_product_via_post(self):
        payload = {"name": "Book", "price": 20.0}

        response = self.client.post(
            "/products/",
            data=json.dumps(payload),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data["name"], "Book")
        self.assertEqual(data["price"], 20.0)
        self.assertTrue(ProductModel.objects.filter(id=data["id"]).exists())


    def test_list_products_via_get(self):
        ProductModel.objects.create(
            id="00000000-0000-0000-0000-000000000001",
            name="Keyboard",
            price=99.10,
        )

        response = self.client.get("/products/")

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        # self.assertGreaterEqual(len(data), 1)
        names = {p["name"] for p in data}
        self.assertIn("Keyboard", names)