from django.db import models

NULLABLE = {"blank": True, "null": True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(**NULLABLE, verbose_name="Описание")
    image_ph = models.ImageField(
        upload_to="products/", **NULLABLE, verbose_name="Изображение(превью)"
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        **NULLABLE,
        related_name="products",
    )
    price = models.IntegerField(verbose_name="Цена за покупку")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["category"]


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование")
    description = models.TextField(**NULLABLE, verbose_name="Описание")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name="заголовок")
    slug = models.CharField(max_length=50, verbose_name="slug")
    description = models.TextField(**NULLABLE, verbose_name="содержимое")
    image_ph = models.ImageField(
        upload_to="blog/", **NULLABLE, verbose_name="Изображение(превью)"
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    is_active = models.BooleanField(default=False)
    views_counter = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"

