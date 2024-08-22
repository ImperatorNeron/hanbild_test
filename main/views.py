from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from main.forms import OnlineApplicationForm
from django.views.generic import FormView
from main.utils import contact_form_errors, create_user_message
from product.models import Service


class BaseApplicationFormView(FormView):
    """
    Base view for applying feedback form in every page
    """

    form_class = OnlineApplicationForm
    title = "HanBild.com.ua"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = self.title
        return context

    def form_valid(self, form):
        return create_user_message(form)

    def form_invalid(self, form):
        return contact_form_errors(form)


class IndexView(BaseApplicationFormView):
    """
    Main page view
    """

    template_name = "main/index.html"
    success_url = reverse_lazy("main:index")
    title = _("Виробництво причепів: замовити виготовлення кузовів в Україні - HanBild")


class ContactsView(BaseApplicationFormView):
    """
    Contact page view
    """

    template_name = "main/contact_us.html"
    success_url = reverse_lazy("main:contacts")
    title = _("Контактна інформація компанії з виготовлення причепів та напівпричепів | HanBild ")


class ServicesView(BaseApplicationFormView):
    """
    Services page view
    """

    template_name = "main/services.html"
    success_url = reverse_lazy("main:services")
    title = _("Послуги HanBild: виробництво та обслуговування причепів та напівпричепів")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["services"] = Service.objects.all().order_by("index_on_page")
        return context


class DeliveryView(BaseApplicationFormView):
    template_name = "main/delivery.html"
    success_url = reverse_lazy("main:delivery")
    title = _("Доставка HanBild: інформація про умови та варіанти доставки причепів та напівпричепів")


class PrivacyPolicyView(BaseApplicationFormView):
    """
    Privacy page view
    """

    template_name = "main/privacy_policy.html"
    success_url = reverse_lazy("main:privacy_policy")
    title = _("Політика конфіденційності HanBild: надійний захист персональних даних")


def page404exception(request, exception):
    """404 exeption handler"""
    return render(request, "main/page404.html", status=404)

