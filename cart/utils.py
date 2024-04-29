from cart.models import Cart


def get_user_carts(request):
    """Function for getting all user carts(items)"""
    if not request.session.session_key:
        request.session.create()
    return Cart.objects.filter(session_key=request.session.session_key).select_related(
        "item"
    ).order_by("-created_timestamp")
