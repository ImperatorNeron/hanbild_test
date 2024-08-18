from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from catalog.models import (
    Goods,
    GoodsCharacteristic,
    GoodsImage,
    GoodsVideo,
)
from catalog.utils import check_filters
from main.views import BaseApplicationFormView


class CatalogView(BaseApplicationFormView):
    """
    Catalog page view
    """

    template_name = "catalog/catalog.html"
    success_url = reverse_lazy("catalog:catalog")
    title = _("Каталог продукції: причепи, кузови та самоскиди від HanBild")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # Get all goods using filters
        context["goods"] = check_filters(self.request)
        return context


class ItemView(BaseApplicationFormView):
    """
    Catalog item page view
    """

    template_name = "catalog/item.html"
    success_url = reverse_lazy("catalog:item")

    def get(self, request, item_slug, *args, **kwargs):
        # Get all item content
        item = Goods.objects.get(slug=item_slug)
        item_photos = GoodsImage.objects.filter(good=item)
        item_videos = GoodsVideo.objects.filter(good=item)
        item_characteristics = GoodsCharacteristic.objects.filter(good=item)
        return render(
            request,
            self.template_name,
            {
                "item": item,
                "item_photos": item_photos,
                "item_videos": item_videos,
                "item_characteristics": item_characteristics,
                "title": f"{item.name} | HanBild.com.ua",
            },
        )

    def dispatch(self, request, *args, **kwargs):
        """
        Function needs for reverse to the same page after appluing form
        """
        self.success_url = reverse_lazy(
            "catalog:item", kwargs={"item_slug": kwargs["item_slug"]}
        )
        return super().dispatch(request, *args, **kwargs)
