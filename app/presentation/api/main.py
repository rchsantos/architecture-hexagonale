from fastapi import FastAPI

from app.presentation.api.routers import products

app = FastAPI(
    title="Hexagonal Architecture + FastAPI",
    description="Example d'intégration propre d'une API hexagonale.",
    version="1.0",
)

app.include_router(products.router)

@app.get("/")
def root():
    return {"message": "Hexagonal Architecture + FastAPI is running"}