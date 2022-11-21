from django.db import models
from drf_util.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=80)
    price = models.IntegerField()
    image = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

