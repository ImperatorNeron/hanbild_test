# Generated by Django 4.2.10 on 2024-08-19 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0010_product_addition_paragraph_ru_product_paragraph_ru_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="description",
            field=models.TextField(
                blank=True, null=True, verbose_name="Опис для метатегу"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="description_en",
            field=models.TextField(
                blank=True, null=True, verbose_name="Опис для метатегу"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="description_ru",
            field=models.TextField(
                blank=True, null=True, verbose_name="Опис для метатегу"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="description_uk",
            field=models.TextField(
                blank=True, null=True, verbose_name="Опис для метатегу"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="title",
            field=models.CharField(
                blank=True, max_length=250, null=True, verbose_name="Назва сторінки"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="title_en",
            field=models.CharField(
                blank=True, max_length=250, null=True, verbose_name="Назва сторінки"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="title_ru",
            field=models.CharField(
                blank=True, max_length=250, null=True, verbose_name="Назва сторінки"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="title_uk",
            field=models.CharField(
                blank=True, max_length=250, null=True, verbose_name="Назва сторінки"
            ),
        ),
    ]