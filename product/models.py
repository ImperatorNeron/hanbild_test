from django.core.validators import MinValueValidator
from django.db import models

from catalog.models import Categories
from embed_video.fields import EmbedVideoField

from hanbild.utils import set_translation_attrs


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
        blank=True,
        null=True,
        verbose_name="Додатковий текст",
    )
    title = models.CharField(
        max_length=250,
        verbose_name="Назва сторінки",
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name="Опис для метатегу",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "product"
        verbose_name = "продукт"
        verbose_name_plural = "Продукцію"

    def save(self, *args, **kwargs):
        set_translation_attrs(self, ("paragraph",))
        set_translation_attrs(
            self,
            ("addition_paragraph",),
            self.addition_paragraph_uk,
        )
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
        set_translation_attrs(self, ("name", "description"))
        return super().save(*args, **kwargs)
