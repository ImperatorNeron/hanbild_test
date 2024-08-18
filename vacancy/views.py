from django.urls import reverse_lazy
from main.views import BaseApplicationFormView
from django.utils.translation import gettext_lazy as _

from vacancy.models import Vacancy, VacancyDescription


class VacancyView(BaseApplicationFormView):
    """
    View class for displaying the vacancies page.
    """

    template_name = "vacancy/vacancy_page.html"
    success_url = reverse_lazy("vacancy:vacancy")
    title = _("Актуальні вакансії: робота в компанії з виробництва причепів та напівпричепів HanBild")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["vacancies"] = Vacancy.objects.all()
        context["vacancies_description"] = VacancyDescription.objects.order_by("choice")
        return context
