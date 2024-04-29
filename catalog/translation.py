from modeltranslation.translator import register, TranslationOptions
from .models import Categories, Goods, GoodsCharacteristic


@register(Categories)
class CategoriesTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Goods)
class GoodsTranslationOptions(TranslationOptions):
    fields = ("name", "description")


@register(GoodsCharacteristic)
class GoodsCharacteristicTranslationOptions(TranslationOptions):
    fields = ("name", "description")