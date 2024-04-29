from django.contrib import admin

from vacancy.models import Vacancy, VacancyDescription
from modeltranslation.admin import TranslationAdmin


class VacancyDescriptionTabulareAdmin(admin.TabularInline):
    model = VacancyDescription
    fields = (
        "choice",
        "text_uk",
        "text_en",
    )


@admin.register(Vacancy)
class ProductAdmin(TranslationAdmin):
    list_display = (
        "id",
        "position_uk",
        "position_en",
        "min_salary",
        "max_salary",
    )
    list_display_links = ("id",)
    list_editable = (
        "position_uk",
        "position_en",
        "min_salary",
        "max_salary",
    )
    fields = (
        ("position_uk", "position_en"),
        ("min_salary", "max_salary"),
    )
    inlines = (VacancyDescriptionTabulareAdmin,)
