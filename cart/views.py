from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View

from cart.models import Cart
from cart.utils import get_user_carts
from catalog.models import Goods
from main.views import BaseApplicationFormView
from django.utils.translation import gettext_lazy as _


class CardAddView(View):
    """Card view to add item in cart which interact with ajax"""

    def post(self, request):
        """Function for adding item to cart"""
        item = Goods.objects.get(id=request.POST.get("product_id"))
        carts = Cart.objects.filter(session_key=request.session.session_key, item=item)
        if carts.exists():
            if cart := carts.first():
                cart.quantity += 1
                cart.save()
        else:
            # Create apart record in db
            Cart.objects.create(
                session_key=request.session.session_key, item=item, quantity=1
            )

        return JsonResponse(
            {
                "message": _("Товар доданий в корзину"),
            }
        )


class CartChangeView(View):
    """Card view to change item in cart which interact with ajax"""

    def post(self, request):
        cart = Cart.objects.get(id=request.POST.get("cart_id"))
        cart.quantity = request.POST.get("quantity")
        cart.save()
        user_carts = get_user_carts(request)
        # if do some action - change part of html template
        string_html = render_to_string(
            "cart/includes/_included_cart.html", {"carts": user_carts}, request=request
        )
        return JsonResponse(
            {
                "cart_items_html": string_html,
                "total_quantity": user_carts.total_quantity(),
            }
        )


class CartRemoveView(View):
    """Card view to remove item from cart which interact with ajax"""

    def post(self, request):
        try:
            Cart.objects.get(id=request.POST.get("cart_id")).delete()
        except Cart.DoesNotExist:
            print("Помилка: об'єкт не знайдено!")
        user_carts = get_user_carts(request)
        string_html = render_to_string(
            "cart/includes/_included_cart.html",
            {"carts": user_carts},
            request=request,
        )
        return JsonResponse(
            {
                "message": _("Товар видалено з корзини"),
                "cart_items_html": string_html,
                "total_quantity": user_carts.total_quantity(),
            }
        )


class UserCartsRemoveView(View):
    """Card view to remove all user carts"""

    def post(self, request):
        session_key = request.session.session_key
        try:
            carts = Cart.objects.filter(session_key=session_key)
            carts.delete()
        except Cart.DoesNotExist:
            print("Помилка: об'єкти не знайдено!")
        except Exception as e:
            print(f"Помилка: {e}")
        return JsonResponse({})


class CartView(BaseApplicationFormView):
    """Cart page view"""

    template_name = "cart/cart.html"
    success_url = reverse_lazy("cart:cart")
    title = _("Корзина")
