from django.urls import path

from order import views

app_name = "order"

urlpatterns = [
    path("", views.OrderView.as_view(), name="order"),
    path("success-order/", views.SuccessOrderView.as_view(), name="success-order"),
]
