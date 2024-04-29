from django.urls import path

from catalog import views

app_name = "catalog"

urlpatterns = [
    path("", views.CatalogView.as_view(), name="catalog"),
    path("", views.CatalogView.as_view(), name="search"),
    path("<slug:item_slug>", views.ItemView.as_view(), name="item"),
]
