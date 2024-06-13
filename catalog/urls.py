from django.urls import path
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from catalog.views import ProductsListView, ProductsDetailView, contact, BlogPostListView, PostCreateView, \
    PostDetailView, PostUpdateView, PostDeleteView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ProductUpdateIsPublishedView, ProductUpdateDescriptionView, ProductUpdateCategoryView, CategoryListView, \
    CategoryDetailView

urlpatterns = [
    path("", TemplateView.as_view(template_name='catalog/index.html'), name='home'),
    path("contact/", contact, name='contact'),
    path("products_list/", ProductsListView.as_view(), name='products'),
    path("blog_post/", BlogPostListView.as_view(), name='blog_post'),
    path("product/<int:pk>/", cache_page(60)(ProductsDetailView.as_view()), name='products_detail'),
    path("create/", PostCreateView.as_view(), name='post_create'),
    path("blog_post/<int:pk>/", PostDetailView.as_view(), name='post_detail'),
    path("<int:pk>/update/", PostUpdateView.as_view(), name='post_update'),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name='post_delete'),
    path("product_create/", ProductCreateView.as_view(), name='product_create'),
    path('update_product/<int:pk>/', ProductUpdateView.as_view(), name="update_product"),

    path('update_product_is_published/<int:pk>/', ProductUpdateIsPublishedView.as_view(),
         name="update_product_is_published"),
    path('update_product_description/<int:pk>/', ProductUpdateDescriptionView.as_view(),
         name="update_product_description"),
    path('update_product_category/<int:pk>/', ProductUpdateCategoryView.as_view(), name="update_product_category"),

    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name="delete_product"),
    path("category_list/", CategoryListView.as_view(), name='сategory'),
    path("category/<int:pk>/", CategoryDetailView.as_view(), name='сategory_detail'),
]
