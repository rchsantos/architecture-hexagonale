# Architecture Hexagonale en Python, FastAPI et Django

Ce dépôt accompagne une série d’articles Medium sur l’architecture hexagonale appliquée à Python.

## 🧩 Partie 1 — Python (domaine pur & hexagone)

Cette branche `part-1-python-core` contient :

- un **domaine métier pur** (`app/domain`)
- des **ports** (`app/application/ports.py`)
- des **cas d’utilisation** (`app/application/use_cases.py`)
- un **adaptateur en mémoire** (`app/infrastructure/adapters/in_memory_product_repository.py`)
- des **tests unitaires** (`tests/test_product_service.py`)
- un petit **exemple CLI** (`app/presentation/cli.py`)

Tout est 100% indépendant de FastAPI, Django ou de toute base de données.

👉 L’article détaillé (version Members) qui explique le code étape par étape :  
**“Comprendre l’Architecture Hexagonale en Python”**  
https://medium.com/@rpsantos/comprendre-larchitecture-hexagonale-en-python-97973bbe9953

---

## 🚀 Lancer le projet

### Installation

```bash
python -m venv .venv
source .venv/bin/activate  # sous Windows: .venv\Scripts\activate
pip install -r requirements.txt
