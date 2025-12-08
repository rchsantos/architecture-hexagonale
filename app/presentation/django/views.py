import json

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View

from app.application.use_cases import ProductService
from app.infrastructure.adapters.django_orm.product_repository import DjangoProductRepository


class ProductView(View):


    @property
    def service(self):
        """
        Instance of DjangoProductRepository
        :return:
        """
        return ProductService(DjangoProductRepository())


    def get(self, request: HttpRequest) -> HttpResponse:
        products = self.service.list_products()
        data = [product.model_dump() for product in products]
        return JsonResponse(data, safe=False)


    def post(self, request: HttpRequest) -> HttpResponse:
        payload = json.loads(request.body)
        product = self.service.create_product(
            name=payload['name'],
            price=payload['price']
        )
        return JsonResponse(product.model_dump(), safe=False, status=201)

