from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from catalog.models import (
    Categories,
    Goods,
    GoodsCharacteristic,
    GoodsImage,
    GoodsVideo,
)


class GoodsImagesTabularAdmin(admin.TabularInline):
    model = GoodsImage
    fields = (
        "good",
        "image",
        "alt_uk",
        "alt_en",
        "alt_ru",
    )
    search_fields = ("good",)


class GoodsVideosTabularAdmin(admin.TabularInline):
    model = GoodsVideo
    fields = ("good", "video")
    search_fields = ("good",)


class GoodsCharacteristicTabularAdmin(admin.TabularInline):
    model = GoodsCharacteristic
    fields = (
        "good",
        "name_uk",
        "description_uk",
        "name_ru",
        "description_ru",
        "name_en",
        "description_en",
    )
    search_fields = (
        "good",
        "name",
    )


class GoodsTabularAdmin(admin.TabularInline):
    model = Goods
    readonly_fields = (
        "name",
        "price",
        "upload_time",
    )
    fields = (
        "name",
        "price",
        "upload_time",
    )
    search_fields = (
        "name",
        "price",
    )
    extra = 0


@admin.register(Categories)
class CategoriesAdmin(TranslationAdmin):
    prepopulated_fields = {"slug": ("name",)}
    fields = (
        ("index_on_page", "slug"),
        "name_uk",
        "name_ru",
        "name_en",
    )
    list_display = (
        "id",
        "index_on_page",
        "name_uk",
        "slug",
    )
    list_display_links = (
        "id",
        "name_uk",
    )
    list_editable = ("index_on_page", "slug")
    inlines = (GoodsTabularAdmin,)


@admin.register(Goods)
class GoodsAdmin(TranslationAdmin):
    exclude = ("slug",)
    list_display = (
        "name",
        "category",
        "price",
        "upload_time",
    )
    list_display_links = (
        "name",
        "price",
        "upload_time",
    )
    list_editable = ("category",)
    fields = (
        "category",
        "name_uk",
        "name_ru",
        "name_en",
        "price",
        "preview_image",
        "preview_alt_uk",
        "preview_alt_en",
        "preview_alt_ru",
        "description_uk",
        "description_ru",
        "description_en",
        "meta_title_uk",
        "meta_title_en",
        "meta_title_ru",
        "meta_description_uk",
        "meta_description_en",
        "meta_description_ru",
    )
    inlines = (
        GoodsCharacteristicTabularAdmin,
        GoodsImagesTabularAdmin,
        GoodsVideosTabularAdmin,
    )
    list_filter = ("upload_time", "category")
