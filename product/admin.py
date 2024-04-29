from django.contrib import admin

from product.models import (
    Product,
    ProductCharacteristics,
    ProductPhotos,
    ProductVideos,
    Service,
)
from modeltranslation.admin import TranslationAdmin


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("index_on_page", "service_name")
    list_editable = ("index_on_page",)
    list_display_links = ("service_name",)
    fields = (
        "index_on_page",
        ("service_name_uk", "service_name_en"),
        ("service_description_uk", "service_description_en"),
        "service_image",
    )


class ProductCharacteristicsTabulareAdmin(admin.TabularInline):
    model = ProductCharacteristics
    fields = (
        "name_uk",
        "name_en",
        "description_uk",
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
