from django.urls import path, re_path
from django.views.generic import TemplateView

from main import views

app_name = "main"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("contacts/", views.ContactsView.as_view(), name="contacts"),
    path("delivery/", views.DeliveryView.as_view(), name="delivery"),
    path("privacy-policy/", views.PrivacyPolicyView.as_view(), name="privacy_policy"),
    re_path(r'^robots\.txt$', TemplateView.as_view(template_name="config/robots.txt", content_type="text/plain")),
    re_path(r'^sitemap\.xml$', TemplateView.as_view(template_name="config/sitemap.xml", content_type="application/xml")),
]
