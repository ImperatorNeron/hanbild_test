# Generated by Django 4.2.10 on 2024-04-12 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="paragraph_en",
            field=models.TextField(null=True, verbose_name="Абзац тексту"),
        ),
        migrations.AddField(
            model_name="product",
            name="paragraph_uk",
            field=models.TextField(null=True, verbose_name="Абзац тексту"),
        ),
    ]
