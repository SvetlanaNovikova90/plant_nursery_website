# Generated by Django 5.0.4 on 2024-05-11 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_blogpost"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="views_counter",
            field=models.IntegerField(default=0, verbose_name="Счетчик просмотров"),
        ),
    ]
