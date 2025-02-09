from django.urls import path
from .views import HomeView, ContactsView, ProductInfoView, ProductCreateView, ProductUpdateView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/<int:pk>/', ProductInfoView.as_view(), name='product_info'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),
]
