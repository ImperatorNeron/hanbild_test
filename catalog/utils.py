import uuid
from deep_translator import GoogleTranslator
from django.core.paginator import Paginator
from django.utils.text import slugify
from django.db.models import Q


def translate_to_en(to_field):
    """
    Translate field into English
    :param to_field: text in Ukrainian
    :return: translated text or None
    """
    return GoogleTranslator(source="auto", target="en").translate(to_field)


def translate_goods(instance):
    """
    Translate goods name and description to English if not already translated
    :param instance: Goods instance
    """
    if not instance.name_en:
        instance.name_en = translate_to_en(instance.name_uk)

    if not instance.description_en:
        instance.description_en = translate_to_en(instance.description_uk)


def translate_categories(instance):
    """
    Translate category name to English if not already translated
    :param instance: Category instance
    """
    if not instance.name_en:
        instance.name_en = translate_to_en(instance.name_uk)


def validate_slug(obj):
    """Function check if exist the same slug. If exist than add uuid4 part"""
    from catalog.models import Goods

    slug = slugify(obj.name_en)
    if not obj.slug:
        if not obj.pk and len(Goods.objects.filter(slug=slug)):
            obj.slug = f"{slug}-{uuid.uuid4().hex[:8]}"
        else:
            obj.slug = slug


def filter_categories(request, result):
    """Check all categoties which are choosen in filter sidebar"""
    keys_list = list(request.GET.keys())

    if "sort_by" in keys_list:
        keys_list.remove("sort_by")
    if "q" in keys_list:
        keys_list.remove("q")
    if "page" in keys_list:
        keys_list.remove("page")
    if "left_range" in keys_list and "right_range" in keys_list:
        keys_list.remove("left_range")
        keys_list.remove("right_range")
    if "quantity" in keys_list:
        keys_list.remove("quantity")

    if keys := keys_list:
        qeary = Q()
        for key in keys:
            print(key)
            qeary |= Q(category__slug=key)
        return result.filter(qeary)
    return result


def q_search(request, result):
    """Function for search specific items in catalog"""

    query = request.GET.get("q", None)
    if not query:
        return result
    if query.isdigit() and len(query) <= 3:
        return result.filter(id=int(query))

    if len(query.split()) == 1:
        return result.filter(name__icontains=query)

    filtered_results = None
    for word in query.split():
        name_filter = Q(name__icontains=word)
        description_filter = Q(description__icontains=word)
        combined_filter = name_filter | description_filter
        if filtered_results is None:
            filtered_results = result.filter(combined_filter)
        else:
            filtered_results = filtered_results.union(result.filter(combined_filter))

    return filtered_results


def sorting_filter(request):
    """Function for price order filter"""
    from catalog.models import Goods

    match request.GET.get("sort_by", None):
        case "price-increase":
            return Goods.objects.order_by("price")
        case "price-decrease":
            return Goods.objects.order_by("-price")
        case _:
            return Goods.objects.order_by("-upload_time")


def price_filter(request, result):
    """Function for price range filter"""
    left_range = request.GET.get("left_range", None)
    right_range = request.GET.get("right_range", None)
    if left_range and right_range:
        return result.filter(
            Q(price__gte=int(left_range)) & Q(price__lte=int(right_range))
        )
    return result


def pagination(request, result):
    """Function for pagination"""
    item_quantity = request.GET.get("quantity", 6)
    paginator = Paginator(result, item_quantity)
    return paginator.get_page(request.GET.get("page", 1))


def check_filters(request):
    """Function connect all filters"""
    try:
        objects = sorting_filter(request)
        objects = filter_categories(request, objects)
        objects = price_filter(request, objects)
        objects = q_search(request, objects)
        objects = pagination(request, objects)
        return objects
    except Exception as e:
        print(f"Filter error: {e}")
