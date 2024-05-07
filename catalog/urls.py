from django.urls import path

from catalog.views import home, contact, products, products_detail

urlpatterns = [
    path("", home, name='home'),
    path("contact/", contact, name='contact'),
    path("products/", products),
    path("products/<int:pk>/", products_detail, name='products_detail'),
]
