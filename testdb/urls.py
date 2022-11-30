from django.urls import path
from . import views

app_name = 'testdb'

urlpatterns = [
    path('', views.ProductCreateAPIView.as_view()),
    path('products/', views.ProductListAPIView.as_view(), name="products"),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name="edit_product"),
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view(), name="delete_product")
]
