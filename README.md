# Architecture Hexagonale en Python : FastAPI & Django

Ce dépôt accompagne une série de trois articles Medium sur l'architecture hexagonale appliquée à Python avec FastAPI et Django.

## 📚 Série d'articles

Cette série explore comment construire des applications Python modulaires, testables et durables en utilisant l'architecture hexagonale :

1. **[Python & l'Architecture Hexagonale (01/03)](https://medium.com/@rpsantos/comprendre-larchitecture-hexagonale-en-python-97973bbe9953)** — Concepts fondamentaux et domaine pur
2. **[Python & l'Architecture Hexagonale (02/03) FastAPI](https://medium.com/@rpsantos/python-larchitecture-hexagonale-02-03-fastapi-5c44323fcf15)** — Intégration avec FastAPI
3. **[Python & l'Architecture Hexagonale (03/03) Django](https://medium.com/@rpsantos/python-larchitecture-hexagonale-03-03-django-74c21844c8ce)** — Intégration avec Django

## 🚀 Partie 2 — FastAPI (adaptateur primaire)

Cette branche `part-2-fastapi` contient :

- Le **domaine métier pur** de la partie 1 (`app/domain`)
- Les **ports et use cases** (`app/application`)
- L'**adaptateur FastAPI** comme interface HTTP (`app/presentation/api`)
- L'**injection de dépendances FastAPI** (`dependencies.py`)
- Des **tests API** avec TestClient (`tests/test_products_api.py`)
- Un **adaptateur en mémoire** pour les tests (`app/infrastructure/adapters/in_memory`)

FastAPI est utilisé uniquement comme **adaptateur primaire** : il reçoit les requêtes HTTP, appelle les use cases, et renvoie les réponses. Zéro logique métier dans les routes.

👉 L'article détaillé qui explique cette intégration :  
**"Python & l'Architecture Hexagonale (02/03) FastAPI"**  
https://medium.com/@rpsantos/python-larchitecture-hexagonale-02-03-fastapi-5c44323fcf15

---

## 🎯 Objectifs de cette partie

Ce projet démontre comment :

- Structurer **FastAPI comme un adaptateur**, pas comme une architecture
- Utiliser l'**injection de dépendances FastAPI** pour brancher les ports
- Créer des **routes minimalistes** sans logique métier
- Maintenir une **testabilité maximale** avec TestClient
- Préparer plusieurs **adaptateurs interchangeables** (in-memory, SQL, API externe)

## 🏗️ Structure du projet
```
app/
├── domain/                    # Domaine métier pur (zéro dépendance externe)
│   ├── models.py             # Entités du domaine (Product)
│   ├── exceptions.py         # Exceptions métier
│   └── services.py           # Services de domaine
│
├── application/              # Couche application (use cases)
│   ├── ports.py             # Interfaces (ProductRepository)
│   ├── use_cases.py         # Cas d'utilisation (ProductService)
│   └── dto.py               # Data Transfer Objects
│
├── infrastructure/           # Adaptateurs secondaires
│   └── adapters/
│       └── in_memory/       # Repository en mémoire
│           └── in_memory_product_repository.py
│
└── presentation/            # Adaptateurs primaires
    ├── cli.py              # Interface ligne de commande
    └── api/                # Interface HTTP FastAPI
        ├── main.py         # Application FastAPI
        ├── dependencies.py # Injection de dépendances
        └── routers/
            └── products.py # Routes produits
```

## 🚀 Installation et lancement

### Prérequis

- Python 3.12+
- Poetry (gestionnaire de dépendances)

### Installation de Poetry
```bash
# macOS / Linux / WSL
curl -sSL https://install.python-poetry.org | python3 -

# Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

### Installation du projet
```bash
# Cloner le dépôt et basculer sur la branche FastAPI
git clone https://github.com/{{ TON_USERNAME }}/architecture-hexagonale-python.git
cd architecture-hexagonale-python
git checkout part-2-fastapi

# Installer les dépendances avec Poetry
poetry install
```

### Lancer l'API FastAPI
```bash
# Démarrer le serveur de développement
poetry run uvicorn app.presentation.api.main:app --reload

# L'API sera accessible sur http://localhost:8000
# Documentation automatique : http://localhost:8000/docs
```

### Tester l'API
```bash
# Lister les produits
curl http://localhost:8000/products/

# Créer un produit
curl -X POST http://localhost:8000/products/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Python Book", "price": 29.90}'

# Accéder à la documentation interactive
open http://localhost:8000/docs  # macOS
xdg-open http://localhost:8000/docs  # Linux
start http://localhost:8000/docs  # Windows
```

## 🧪 Tests

Le projet utilise pytest avec le TestClient de FastAPI :
```bash
# Lancer tous les tests
poetry run pytest

# Tests du domaine uniquement
poetry run pytest tests/test_product_service.py

# Tests de l'API FastAPI
poetry run pytest tests/test_products_api.py

# Avec coverage
poetry run pytest --cov=app --cov-report=html

# Mode verbose
poetry run pytest -v
```

## 🔑 Concepts clés de cette partie

### FastAPI comme adaptateur primaire

Les routes FastAPI ne contiennent **aucune logique métier** :
```python
@router.post("/", response_model=Product)
def create_product(
    payload: ProductCreateDTO,
    service: ProductService = Depends(get_product_service),
):
    return service.create_product(
        name=payload.name,
        price=payload.price,
    )
```

### Injection de dépendances

FastAPI injecte automatiquement les dépendances :
```python
def get_repository() -> ProductRepository:
    return InMemoryProductRepository()

def get_product_service(
    repo: ProductRepository = Depends(get_repository),
) -> ProductService:
    return ProductService(repository=repo)
```

Cela permet de :
- Changer d'implémentation facilement
- Mocker les dépendances dans les tests
- Éviter tout couplage entre FastAPI et l'application

### Tests sans base de données

Grâce à l'architecture hexagonale, les tests API n'utilisent aucune base de données :
```python
def test_create_product_api():
    response = client.post("/products/", json={"name": "Book", "price": 20})
    assert response.status_code == 201
    assert response.json()["name"] == "Book"
```

## 📦 Dépendances principales

- **pydantic** (>=2.12.5) : Validation et modèles du domaine
- **fastapi** (>=0.123.9) : Framework web asynchrone
- **uvicorn** (>=0.38.0) : Serveur ASGI
- **pytest** (>=9.0.1) : Framework de tests
- **httpx** (>=0.28.1) : Client HTTP pour les tests

## 🌟 Avantages de cette approche

✅ **Routes minimalistes** : Aucune logique métier dans FastAPI

✅ **Testabilité** : Tests API sans base de données ni dépendances externes

✅ **Flexibilité** : Changez de repository (in-memory → SQL → API) sans toucher aux routes

✅ **Documentation automatique** : FastAPI génère Swagger/OpenAPI automatiquement

✅ **Type safety** : Pydantic valide les données en entrée et sortie

## 🔧 Commandes utiles
```bash
# Démarrer avec rechargement automatique
poetry run uvicorn app.presentation.api.main:app --reload

# Démarrer sur un port spécifique
poetry run uvicorn app.presentation.api.main:app --port 8080

# Démarrer avec plusieurs workers (production)
poetry run uvicorn app.presentation.api.main:app --workers 4

# Lancer le CLI (démonstration)
poetry run python app/presentation/cli.py
```

## 📖 Prochaine étape

La **partie 3** intègre Django comme adaptateur, en conservant exactement le même domaine et les mêmes use cases.

👉 [Lire l'article Django](https://medium.com/@rpsantos/python-larchitecture-hexagonale-03-03-django-74c21844c8ce)

## 👤 Auteur

**Richardson Santos**
- Software Engineer avec +10 ans d'expérience
- [LinkedIn](https://www.linkedin.com/in/richardsonsantos/)
- [Medium](https://medium.com/@rpsantos)

## 📝 Licence

Ce projet est fourni à des fins éducatives. N'hésitez pas à l'utiliser, le modifier et l'adapter à vos besoins.

---

💡 **Vous avez trouvé ce projet utile ?** N'hésitez pas à mettre une ⭐ sur le dépôt et à partager vos retours !
