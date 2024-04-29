from django.urls import path

from vacancy import views

app_name = "vacancy"

urlpatterns = [
    path("", views.VacancyView.as_view(), name="vacancy"),
]
