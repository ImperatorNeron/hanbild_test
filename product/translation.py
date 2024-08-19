from modeltranslation.translator import register, TranslationOptions
from .models import Product, ProductCharacteristics, Service


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ("paragraph", "addition_paragraph", "title", "description")


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ("service_name", "service_description")


@register(ProductCharacteristics)
class ProductCharacteristicsTranslationOptions(TranslationOptions):
    fields = ("name", "description")

