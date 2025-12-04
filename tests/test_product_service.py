from app.application.use_cases import ProductService
from app.domain.exceptions import ProductNotFound
from app.infrastructure.adapters.in_memory_product_repository import InMemoryProductRepository


def test_create_and_list_products():
    repo = InMemoryProductRepository()
    service = ProductService(repo)

    assert service.list_products() == []

    product = service.create_product(name="Test Product", price=10.0)

    products = service.list_products()
    assert len(products) == 1
    assert products[0].id == product.id
    assert products[0].name == "Test Product"
    assert products[0].price == 10.0


def test_get_product_by_id():
    repo = InMemoryProductRepository()
    service = ProductService(repo)

    try:
        service.get_product("unknown-id")
        assert False, "Expected ProductNotFound"
    except ProductNotFound as e:
        assert e.product_id == "unknown-id"