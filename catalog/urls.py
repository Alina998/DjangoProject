from django.urls import path
from .views import HomeView, ContactsView, ProductsByCategoryView, ProductInfoView, ProductCreateView, ProductUpdateView, ProductDeleteView
from catalog.apps import CatalogConfig
from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/<int:pk>/', cache_page(60)(ProductInfoView.as_view()), name='product_info'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),
    path('products/<int:pk>/unpublish_product/', ProductUpdateView.as_view(), name='unpublish_product'),
    path('category/<int:category_id>', ProductsByCategoryView.as_view(), name='products_by_category'),
]
