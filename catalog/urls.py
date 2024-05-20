from django.urls import path
from django.views.generic import TemplateView

from catalog.views import ProductsListView, ProductsDetailView, contact, BlogPostListView, PostCreateView, \
    PostDetailView, PostUpdateView, PostDeleteView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path("", TemplateView.as_view(template_name='catalog/index.html'), name='home'),
    path("contact/", contact, name='contact'),
    path("products_list/", ProductsListView.as_view(), name='products'),
    path("blog_post/", BlogPostListView.as_view(), name='blog_post'),
    path("product/<int:pk>/", ProductsDetailView.as_view(), name='products_detail'),
    path("create/", PostCreateView.as_view(), name='post_create'),
    path("blog_post/<int:pk>/", PostDetailView.as_view(), name='post_detail'),
    path("<int:pk>/update/", PostUpdateView.as_view(), name='post_update'),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name='post_delete'),
    path("product_create/", ProductCreateView.as_view(), name='product_create'),
    path("<int:pk>/product_update/", ProductUpdateView.as_view(), name='product_update'),
    path("product_delete/<int:pk>/", ProductDeleteView.as_view(), name='product_delete')
]
