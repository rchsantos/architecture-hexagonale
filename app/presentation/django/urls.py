from django.urls import path
from app.presentation.django.views import ProductView

urlpatterns = [
    path("products/", ProductView.as_view(), name="products"),
]