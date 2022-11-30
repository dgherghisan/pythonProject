from .models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=80,
        style={'input_type': 'text'}
    )
    price = serializers.IntegerField()

    image = serializers.ListField(child=serializers.ImageField(use_url="images/"))

    class Meta:
        model = Product
        fields = [
            "pk",
            "name",
            "price",
            "image",
            "author"
        ]
