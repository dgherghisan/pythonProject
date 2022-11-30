from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all().order_by('created_at')
    serializer_class = ProductSerializer
    template_name = 'create_product.html'
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        image = serializer.validated_data.get("image")
        name = serializer.validated_data.get("name")
        price = serializer.validated_data.get("price")
        author = self.request.user

        obj_list = []
        for img in image:
            obj_list.append(Product(name=name, price=price, image=img, author=author))

        if obj_list:
            Product.objects.bulk_create(obj_list)


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all().order_by('created_at')
        return Response({'queryset': queryset}, template_name='view_products.html')


class ProductUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Product.objects.all().order_by('created_at')
    serializer_class = ProductSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAuthenticated]


class ProductDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Product.objects.all().order_by('created_at')
    serializer_class = ProductSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAuthenticated]
