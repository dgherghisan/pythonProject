from django.urls import path
from . import views

app_name = 'testdb'

urlpatterns = [
    path('', views.create_product, name='create_product'),
    path('products/', views.view_product, name='view_product'),
    path('products/delete/<int:id>', views.delete_product, name='delete_product'),
    path('products/edit/<int:id>', views.edit_product, name='edit_product')
]
