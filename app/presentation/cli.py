from app.application.use_cases import ProductService
from app.infrastructure.adapters.in_memory_product_repository import InMemoryProductRepository


def main() -> None:
    repository = InMemoryProductRepository()
    service = ProductService(repository=repository)

    # Création de quelques produits
    service.create_product(name="Python Book", price=29.90)
    service.create_product(name="Mechanical Keyboard", price=120.0)


    # Affichage
    products = service.list_products()
    print("Products in System:")
    for product in products:
        print(f"- {product.id} | {product.name} | {product.price}€")



if __name__ == "__main__":
    main()