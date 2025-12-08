import uuid

from django.db import models


class ProductModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.FloatField()

    class Meta:
        db_table = "product"