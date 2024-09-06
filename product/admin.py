from django.contrib import admin

from product.models import (
    Product,
    ProductCharacteristics,
    ProductPhotos,
    ProductVideos,
)
from modeltranslation.admin import TranslationAdmin


class ProductCharacteristicsTabulareAdmin(admin.TabularInline):
    model = ProductCharacteristics
    fields = (
        "name_uk",
        "description_uk",
        "name_ru",
        "description_ru",
        "name_en",
        "description_en",
    )


class ProductVideosTabulareAdmin(admin.TabularInline):
    model = ProductVideos
    fields = ("video",)


class ProductPhotosTabulareAdmin(admin.TabularInline):
    model = ProductPhotos
    fields = ("image",)


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = (
        "index_on_page",
        "category",
    )
    list_display_links = ("category",)
    list_editable = ("index_on_page",)
    inlines = (
        ProductCharacteristicsTabulareAdmin,
        ProductVideosTabulareAdmin,
        ProductPhotosTabulareAdmin,
    )
