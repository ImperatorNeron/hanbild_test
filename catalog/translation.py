from modeltranslation.translator import register, TranslationOptions
from .models import Categories, Goods, GoodsCharacteristic, GoodsImage


@register(Categories)
class CategoriesTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Goods)
class GoodsTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "description",
        "preview_alt",
        "meta_title",
        "meta_description",
    )


@register(GoodsImage)
class GoodsImagesTranslationOptions(TranslationOptions):
    fields = ("alt",)


@register(GoodsCharacteristic)
class GoodsCharacteristicTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "description",
    )
