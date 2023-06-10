from django.db import models
from drf_util.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to="images/", default=[])
    author = models.CharField(max_length=200, default="")
