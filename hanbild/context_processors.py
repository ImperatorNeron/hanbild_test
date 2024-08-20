from django.utils.translation import get_language


def hreflang_processor(request):
    current_url = request.path
    hreflangs = {
        "en": f"https://www.hanbild.com.ua/en{current_url}",
        "ru": f"https://www.hanbild.com.ua/ru{current_url}",
        "uk": f"https://www.hanbild.com.ua{current_url}",
    }
    canonical_url = hreflangs[get_language()]

    return {
        "hreflangs": hreflangs,
        "canonical_url": canonical_url,
    }
