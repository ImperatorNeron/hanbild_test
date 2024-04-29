from django.core.validators import MinValueValidator
from django.db import models

from catalog.models import Categories
from catalog.utils import translate_goods
from product.utils import translate_product_paragraph, translate_service
from embed_video.fields import EmbedVideoField


class Product(models.Model):
    category = models.OneToOneField(
        to=Categories,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Категорія",
    )
    index_on_page = models.IntegerField(
        verbose_name="Порядковий номер", validators=[MinValueValidator(0)], default=0
    )
    paragraph = models.TextField(verbose_name="Основний текст")
    paragraph_image = models.ImageField(
        upload_to="categories_images", verbose_name="Фото до основного тексту"
    )
    addition_paragraph = models.TextField(
        blank=True, null=True, verbose_name="Додатковий текст"
    )

    class Meta:
        db_table = "product"
        verbose_name = "продукт"
        verbose_name_plural = "Продукцію"

    def save(self, *args, **kwargs):
        translate_product_paragraph(self)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Продукт категорії: '{self.category}'"


class ProductPhotos(models.Model):
    category = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Категорія",
    )
    image = models.ImageField(upload_to="categories_images", verbose_name="Фото")

    def __str__(self):
        return f"Фото для категорії: {self.category}"

    class Meta:
        db_table = "product_photo"
        verbose_name = "фото продукції"
        verbose_name_plural = "Фото продукції"


class ProductVideos(models.Model):
    category = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Категорія",
    )
    video = EmbedVideoField(verbose_name="Посилання на відео")

    def __str__(self):
        return f"Відео для категорії: {self.category}"

    class Meta:
        db_table = "product_videos"
        verbose_name = "відео продукції"
        verbose_name_plural = "Відео продукції"


class ProductCharacteristics(models.Model):
    category = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Категорія",
    )
    name = models.CharField(max_length=100, verbose_name="Назва характеристики")
    description = models.CharField(max_length=255, verbose_name="Опис")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "products_characteristics"
        verbose_name = "характеристика продукції"
        verbose_name_plural = "Характеристики продукції"

    def save(self, *args, **kwargs):
        translate_goods(self)
        return super().save(*args, **kwargs)


class Service(models.Model):
    index_on_page = models.IntegerField(
        verbose_name="Порядковий номер", validators=[MinValueValidator(0)], default=0
    )
    service_name = models.CharField(max_length=200, verbose_name="Назва послуги")
    service_description = models.TextField(verbose_name="Опис послуги")
    service_image = models.ImageField(
        upload_to="services_images", verbose_name="Фото послуги"
    )

    class Meta:
        db_table = "service"
        verbose_name = "сервіс"
        verbose_name_plural = "Сервіси"

    def save(self, *args, **kwargs):
        translate_service(self)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.service_name}"
