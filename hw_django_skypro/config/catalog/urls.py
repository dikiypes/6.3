from django.urls import path
from catalog.views import home, contact_view, product_detail
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path("", home),
    path("contact/", contact_view),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
]
