# Architecture Hexagonale en Python, FastAPI et Django

Ce dépôt accompagne une série d'articles Medium sur l'architecture hexagonale :

- Partie 1 : Python (domaine pur, ports & adaptateurs)
- Partie 2 : Intégration FastAPI
- Partie 3 : Intégration Django

## Partie 1 — Python (core hexagonal)

Cette branche (`part-1-python-core`) montre comment :

- définir un domaine métier pur (`app/domain`)
- définir des ports (`app/application/ports.py`)
- implémenter un cas d'utilisation (`app/application/use_cases.py`)
- brancher un adaptateur en mémoire (`app/infrastructure/adapters`)
- tester le tout (`tests/`)

### Installation

```bash
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate sous Windows
pip install -r requirements.txt
pytest
python -m app.presentation.cli
