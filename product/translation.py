from modeltranslation.translator import register, TranslationOptions
from .models import Product, ProductCharacteristics


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ("paragraph", "addition_paragraph", "title", "description")


@register(ProductCharacteristics)
class ProductCharacteristicsTranslationOptions(TranslationOptions):
    fields = ("name", "description")

