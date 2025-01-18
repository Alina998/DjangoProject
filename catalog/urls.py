from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_info, add_product
from django.conf import settings
from django.conf.urls.static import static

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:product_id>/', product_info, name='product_info'),
    path('add_product/', add_product, name='add_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
