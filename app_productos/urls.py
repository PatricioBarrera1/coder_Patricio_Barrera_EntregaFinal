from django.urls import path
from .views import delete_product, list_products, create_product, update_product

app_name = "app_productos"

urlpatterns = [
    path('list/', list_products, name='list_products'),
    path('create/', create_product, name='create_product'),
    path('update/<int:pk>/', update_product, name='update_product'),
    path('delete/<int:pk>/', delete_product, name='delete_product'),
]
