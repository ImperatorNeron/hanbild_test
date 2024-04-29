from modeltranslation.translator import register, TranslationOptions

from vacancy.models import Vacancy, VacancyDescription


@register(Vacancy)
class VacancyTranslationOptions(TranslationOptions):
    fields = ("position",)


@register(VacancyDescription)
class VacancyTranslationOptions(TranslationOptions):
    fields = ("text", )