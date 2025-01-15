from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_info, add_product

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product_info/', product_info, name='product_info'),
    path('add_product/', add_product, name='add_product'),
]
