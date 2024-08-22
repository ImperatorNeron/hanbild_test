from django.conf.urls import handler500
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from hanbild import settings
from hanbild.settings import DEBUG

handler404 = "main.views.page404exception"

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += i18n_patterns(
    path("i18n/", include("django.conf.urls.i18n")),
    path("", include("main.urls", namespace="main")),
    path("catalog/", include("catalog.urls", namespace="catalog")),
    path("cart/", include("cart.urls", namespace="cart")),
    path("product/", include("product.urls", namespace="product")),
    path("order/", include("order.urls", namespace="order")),
    path("vacancies/", include("vacancy.urls", namespace="vacancy")),
    prefix_default_language=False,
)

if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
