from starlette.testclient import TestClient

from app.presentation.api.main import app

client = TestClient(app)


def test_create_product_api():
    response = client.post("/products/", json={"name": "Book", "price": 20})
    assert response.status_code == 201
    assert response.json()
    assert response.json()["name"] == "Book"
    assert response.json()["price"] == 20


def test_list_products_api():
    client.post("/products/", json={"name": "Mouse", "price": 15})
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)