from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.view_product),
    path('', views.create_product)
]
