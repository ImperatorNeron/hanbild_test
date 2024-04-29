from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView

from main.forms import OnlineApplicationForm
from main.utils import contact_form_errors, create_user_message
from main.views import BaseApplicationFormView
from order.forms import CreateOrderForm
from order.utils import create_order_transaction, order_fields_errors


class OrderView(TemplateView):
    """
    View class for displaying order information and interact with it
    """

    template_name = "order/order.html"
    title = _("Оформлення замовлення | HanBild.com.ua")
    # Two forms for correct applying post request
    contact_form = OnlineApplicationForm
    order_form = CreateOrderForm
    success_url = reverse_lazy("order:success-order")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = self.title
        return context

    def form_validation(self, create_function, error_function, form, **kwargs):
        if form.is_valid():
            return create_function(form, **kwargs)
        return error_function(form, **kwargs)

    def post(self, request):
        """
        Check which form was activated
        """
        if request.POST["form-class"] == "order-form":
            return self.form_validation(
                create_order_transaction,
                order_fields_errors,
                self.order_form(request.POST),
                session_key=request.session.session_key,
                success_url=self.success_url,
            )
        elif request.POST["form-class"] == "feedback-form":
            return self.form_validation(
                create_user_message,
                contact_form_errors,
                self.contact_form(request.POST),
            )


class SuccessOrderView(BaseApplicationFormView):
    """
    View class for displaying successful order message
    """

    template_name = "order/success_order.html"
    success_url = reverse_lazy("order:success-order")
    title = _("Замовлення пройшло успішно!")
