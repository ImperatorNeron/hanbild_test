from django.contrib import admin

from vacancy.models import Vacancy, VacancyDescription
from modeltranslation.admin import TranslationAdmin


class VacancyDescriptionTabulareAdmin(admin.TabularInline):
    model = VacancyDescription
    fields = (
        "choice",
        "text_uk",
        "text_ru",
        "text_en",
    )


@admin.register(Vacancy)
class ProductAdmin(TranslationAdmin):
    list_display = (
        "id",
        "position_uk",
        "min_salary",
        "max_salary",
    )
    list_display_links = ("id", "position_uk")
    inlines = (VacancyDescriptionTabulareAdmin,)
