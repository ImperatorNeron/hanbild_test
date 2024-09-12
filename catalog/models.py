from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

from embed_video.fields import EmbedVideoField

from catalog.utils import validate_slug
from hanbild.utils import set_translation_attrs


class Categories(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Назва",
    )
    index_on_page = models.IntegerField(
        verbose_name="Порядковий номер",
        validators=[MinValueValidator(0)],
        default=0,
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        null=True,
        verbose_name="URL",
    )

    class Meta:
        db_table = "category"
        verbose_name = "категорію"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        set_translation_attrs(self, ("name",))
        return super().save(*args, **kwargs)


class Goods(models.Model):
    category = models.ForeignKey(
        to=Categories,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Категорія",
    )
    slug = models.SlugField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="URL",
    )
    name = models.CharField(
        max_length=150,
        verbose_name="Назва товару",
    )
    preview_image = models.ImageField(
        upload_to="goods_images",
        null=True,
        blank=True,
        verbose_name="Зображення",
    )
    preview_alt = models.CharField(
        verbose_name="Alt зображення",
        max_length=255,
        default="",
        blank=True,
        null=True,
    )
    price = models.FloatField(
        verbose_name="Ціна товару",
        default=0,
    )
    currency = models.CharField(
        max_length=1,
        choices=[
            ("$", "Долар"),
            ("€", "Євро"),
            ("₴", "Гривня"),
        ],
        default="$",
        verbose_name="Валюта",
    )
    upload_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата завантаження",
    )
    description = models.TextField(
        verbose_name="Опис товару",
        null=True,
        blank=True,
    )

    meta_title = models.CharField(
        max_length=255,
        verbose_name="Назва сторінки товару",
        blank=True,
        null=True,
    )
    meta_description = models.TextField(
        verbose_name="Опис для метатегу",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"Товар: {self.name} | Категорія: {self.category}"

    class Meta:
        db_table = "goods"
        verbose_name = "товар"
        verbose_name_plural = "Товар"

    def save(self, *args, **kwargs):
        set_translation_attrs(self, ("name", "description"))
        validate_slug(self)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("catalog:item", kwargs={"item_slug": self.slug})


class GoodsImage(models.Model):
    good = models.ForeignKey(to=Goods, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(
        upload_to="goods_images",
        verbose_name="Зображення",
        null=True,
    )
    alt = models.CharField(
        verbose_name="Alt зображення",
        max_length=255,
        blank=True,
        null=True,
        default="",
    )

    def __str__(self):
        return f"{self.good.name} - {self.image.name}"

    class Meta:
        db_table = "goods_images"
        verbose_name = "фотографію товару"
        verbose_name_plural = "Фотографії товару"


class GoodsVideo(models.Model):
    good = models.ForeignKey(to=Goods, on_delete=models.SET_NULL, null=True)
    video = EmbedVideoField(verbose_name="Посилання на відео")

    def __str__(self):
        return f"{self.good.name} - {self.video}"

    class Meta:
        db_table = "goods_videos"
        verbose_name = "відео товару"
        verbose_name_plural = "Відео товару"


class GoodsCharacteristic(models.Model):
    good = models.ForeignKey(to=Goods, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, verbose_name="Назва характеристики")
    description = models.CharField(max_length=255, verbose_name="Опис")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "goods_characteristics"
        verbose_name = "характеристика товару"
        verbose_name_plural = "Характеристики товару"

    def save(self, *args, **kwargs):
        set_translation_attrs(self, ("name", "description"))
        return super().save(*args, **kwargs)
