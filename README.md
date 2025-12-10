# Architecture Hexagonale en Python : FastAPI & Django

Ce dépôt accompagne une série de trois articles Medium sur l'architecture hexagonale appliquée à Python avec FastAPI et Django.

## 📚 Série d'articles

Cette série explore comment construire des applications Python modulaires, testables et durables en utilisant l'architecture hexagonale :

1. **[Python & l'Architecture Hexagonale (01/03)](https://medium.com/@rpsantos/comprendre-larchitecture-hexagonale-en-python-97973bbe9953)** — Concepts fondamentaux et domaine pur
2. **[Python & l'Architecture Hexagonale (02/03) FastAPI](https://medium.com/@rpsantos/python-larchitecture-hexagonale-02-03-fastapi-5c44323fcf15)** — Intégration avec FastAPI
3. **[Python & l'Architecture Hexagonale (03/03) Django](https://medium.com/@rpsantos/python-larchitecture-hexagonale-03-03-django-74c21844c8ce)** — Intégration avec Django

## 🎯 Objectifs du projet

Ce projet démontre comment :

- Structurer un **domaine métier pur**, totalement découplé des frameworks
- Utiliser des **ports & adaptateurs** pour isoler l'infrastructure
- Intégrer **FastAPI** et **Django** comme simples adaptateurs
- Maintenir une **testabilité maximale** sans dépendances externes
- Construire des applications **évolutives** et **maintenables**

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
│   └── use_cases.py         # Cas d'utilisation (ProductService)
│
├── infrastructure/           # Adaptateurs secondaires
│   └── adapters/
│       ├── in_memory/       # Repository en mémoire (tests/démo)
│       └── django_orm/      # Repository Django ORM
│           ├── product_model.py
│           ├── product_mapper.py
│           └── product_repository.py
│
└── presentation/            # Adaptateurs primaires
    ├── cli.py              # Interface ligne de commande
    └── django/             # Interface HTTP Django
        ├── views.py
        └── urls.py
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
# Cloner le dépôt
git clone https://github.com/{{ TON_USERNAME }}/architecture-hexagonale-python.git
cd architecture-hexagonale-python

# Installer les dépendances avec Poetry
poetry install
```

### Lancer la démo CLI
```bash
poetry run python app/presentation/cli.py
```

### Lancer l'application Django
```bash
# Appliquer les migrations
poetry run python manage.py migrate

# Démarrer le serveur
poetry run python manage.py runserver

# Tester l'API
curl http://localhost:8000/products/
curl -X POST http://localhost:8000/products/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Python Book", "price": 29.90}'
```

## 🧪 Tests

Le projet utilise pytest avec support Django :
```bash
# Lancer tous les tests
poetry run pytest

# Tests du domaine uniquement (sans Django)
poetry run pytest tests/test_product_service.py

# Tests de l'adaptateur Django ORM
poetry run pytest tests/test_django_product_repository.py

# Tests des vues Django
poetry run pytest tests/test_django_product_view.py

# Avec coverage
poetry run pytest --cov=app --cov-report=html
```

## 🔧 Commandes Poetry utiles
```bash
# Ajouter une nouvelle dépendance
poetry add nom-du-package

# Ajouter une dépendance de développement
poetry add --group dev nom-du-package

# Mettre à jour les dépendances
poetry update

# Afficher les dépendances installées
poetry show

# Activer l'environnement virtuel
poetry shell

# Exécuter une commande dans l'environnement
poetry run python script.py
```

## 🔑 Concepts clés

### Domaine métier pur

Le domaine ne dépend d'aucun framework. Il contient uniquement :
- Les **entités** (`Product`)
- Les **règles métier** (validations Pydantic)
- Les **exceptions métier** (`ProductNotFound`)

### Ports (interfaces)

Les ports définissent les contrats entre les couches :
```python
class ProductRepository(ABC):
    @abstractmethod
    def get_by_id(self, product_id: str) -> Optional[Product]: ...
    
    @abstractmethod
    def save(self, product: Product) -> None: ...
```

### Adaptateurs

Les adaptateurs implémentent les ports :
- **Adaptateurs primaires** (driving) : CLI, Django views, FastAPI routes
- **Adaptateurs secondaires** (driven) : In-memory repository, Django ORM

### Mappers

Les mappers isolent complètement le domaine de l'infrastructure :
```python
class ProductMapper:
    @staticmethod
    def to_domain(model) -> Product: ...
    
    @staticmethod
    def to_orm(product: Product) -> dict: ...
```

## 📦 Dépendances principales

- **pydantic** (>=2.12.5) : Validation et modèles du domaine
- **django** (>=6.0) : Framework web et ORM
- **pytest** (>=9.0.1) : Framework de tests
- **pytest-django** : Support Django pour pytest

## 🌟 Avantages de cette architecture

✅ **Testabilité** : Testez votre domaine sans base de données ni framework

✅ **Flexibilité** : Changez d'ORM, de framework ou d'infrastructure sans toucher au domaine

✅ **Maintenabilité** : Code organisé, responsabilités claires

✅ **Évolutivité** : Ajoutez de nouveaux adaptateurs sans modifier l'existant

✅ **Indépendance** : Le domaine ne connaît ni Django, ni FastAPI, ni PostgreSQL

## 📖 Pour aller plus loin

- [Documentation officielle sur l'architecture hexagonale](https://alistair.cockburn.us/hexagonal-architecture/)
- [Clean Architecture par Robert C. Martin](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Profil Medium de Richardson Santos](https://medium.com/@rpsantos)

## 👤 Auteur

**Richardson Santos**
- Software Engineer avec +10 ans d'expérience
- [Medium](https://medium.com/@rpsantos)
- LinkedIn: https://www.linkedin.com/in/richardsonsantos/

## 📝 Licence

Ce projet est fourni à des fins éducatives. N'hésitez pas à l'utiliser, le modifier et l'adapter à vos besoins.

---

💡 **Vous avez trouvé ce projet utile ?** N'hésitez pas à mettre une ⭐ sur le dépôt et à partager vos retours !
