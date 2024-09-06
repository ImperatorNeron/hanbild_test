from django.contrib import admin

from solution.models import Solution, SolutionVideos, SolutionPhotos


class SolutionVideosTabularAdmin(admin.TabularInline):
    model = SolutionVideos
    fields = ("video",)


class SolutionPhotosTabularAdmin(admin.TabularInline):
    model = SolutionPhotos
    fields = ("image",)


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("solution_title_uk",)}
    list_display = (
        "id",
        "index_on_page",
        "solution_title",
        "slug"
    )
    list_editable = ("index_on_page", "slug",)
    list_display_links = ("id", "solution_title",)
    fields = (
        "index_on_page",
        "review_image",
        "slug",
        "solution_title_uk",
        "solution_title_en",
        "solution_title_ru",
        "review_content_uk",
        "review_content_en",
        "review_content_ru",
        "content_uk",
        "content_en",
        "content_ru",
        "title_uk",
        "title_en",
        "title_ru",
        "description_uk",
        "description_en",
        "description_ru",
    )
    inlines = (
        SolutionPhotosTabularAdmin,
        SolutionVideosTabularAdmin,
    )
