from modeltranslation.translator import register, TranslationOptions

from solution.models import Solution


@register(Solution)
class SolutionTranslationOptions(TranslationOptions):
    fields = ("title", "description", "solution_title", "review_content", "content")


