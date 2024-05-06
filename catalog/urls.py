from django.urls import path

from catalog.views import home, contact, products, products_detail

urlpatterns = [
    path("", home),
    path("contact/", contact),
    path("products/", products),
    path("product/<int:pk>/", products_detail, name='products_detail'),
]
