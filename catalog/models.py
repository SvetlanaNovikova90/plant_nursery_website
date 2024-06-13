from django.db import models

from users.models import User

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
    )
    price = models.IntegerField(verbose_name="Цена за покупку")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Создатель')

    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["category"]
        permissions = [('can_change_description', 'Can change product description',),
                       ('can_change_category', 'Can change product category',),
                       ('set_published_status', 'Can change product published status',)]


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
    slug = models.CharField(max_length=50, **NULLABLE, verbose_name="slug")
    description = models.TextField(**NULLABLE, verbose_name="содержимое")
    image_ph = models.ImageField(
        upload_to="blog/", **NULLABLE, verbose_name="Изображение(превью)"
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    is_active = models.BooleanField(default=True)
    views_counter = models.IntegerField(default=0, verbose_name="Счетчик просмотров")
    publication_sign = models.BooleanField(default=True, verbose_name='признак публикации')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"
        permissions = [('can_change_publication_sign', 'Can change blog publication_sign',)]


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="version",
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="продукт",
    )
    version_number = models.CharField(max_length=20, verbose_name="номер версии")
    title = models.CharField(max_length=100, verbose_name="название версии")
    is_active = models.BooleanField(**NULLABLE, verbose_name='признак текущей версии')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "версия"
        verbose_name_plural = "версии"
