from django.contrib import admin

from catalog.models import Category, Product, BlogPost, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    # list_filter = список_полей_для_фильтрации
    # search_fields = список_полей_для_поиска


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(BlogPost)
class BlogPost(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "is_active", "views_counter")
    # list_filter = ("category",)
    # search_fields = ("name", "description")


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "product", "version_number", "is_active")
