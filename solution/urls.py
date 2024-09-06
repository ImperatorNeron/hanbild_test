from django.urls import path

from solution import views

app_name = "solution"

urlpatterns = [
    path("", views.SolutionView.as_view(), name="solution"),
    path("<slug:slug>", views.SolutionPageView.as_view(), name="solution_page"),
]
