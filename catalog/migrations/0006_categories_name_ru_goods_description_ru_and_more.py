# Generated by Django 4.2.10 on 2024-08-01 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_categories_index_on_page"),
    ]

    operations = [
        migrations.AddField(
            model_name="categories",
            name="name_ru",
            field=models.CharField(
                max_length=150, null=True, unique=True, verbose_name="Назва"
            ),
        ),
        migrations.AddField(
            model_name="goods",
            name="description_ru",
            field=models.TextField(blank=True, null=True, verbose_name="Опис товару"),
        ),
        migrations.AddField(
            model_name="goods",
            name="name_ru",
            field=models.CharField(
                max_length=150, null=True, verbose_name="Назва товару"
            ),
        ),
        migrations.AddField(
            model_name="goodscharacteristic",
            name="description_ru",
            field=models.CharField(max_length=255, null=True, verbose_name="Опис"),
        ),
        migrations.AddField(
            model_name="goodscharacteristic",
            name="name_ru",
            field=models.CharField(
                max_length=100, null=True, verbose_name="Назва характеристики"
            ),
        ),
    ]
