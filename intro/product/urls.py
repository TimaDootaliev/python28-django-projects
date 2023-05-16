from django.urls import path

from .views import delete_product, get_products, create_product, get_one_product


urlpatterns = [
    path('products/', get_products),
    path('create-product/', create_product),
    path('products/<int:id>/', get_one_product),
    path('delete-product/<int:id>/', delete_product),
]