from deep_translator import GoogleTranslator


def translate_to_language(to_field, lang="en"):
    """
    Translate field in specific language
    :param to_field: text in Ukrainian
    :param lang: goal language
    :return: translated text or None
    """
    try:
        return GoogleTranslator(source="auto", target=lang).translate(to_field)
    except Exception as e:
        print(f"Translation failed: {e}")


def set_translation_attrs(instance, attrs: tuple, extra_condition: bool = True):
    """
    Translate specified attributes to English and russian if not already translated.
    :param instance: object of specific model
    :param attrs: tuple with parameters names
    :param extra_condition: if need to check another instance
    """
    languages = ("en", "ru")
    fields = []

    for i in languages:
        for j in attrs:
            fields.append((f"{j}_uk", f"{j}_{i}", i))

    for source_field, target_field, to_lang in fields:
        if not getattr(instance, target_field) and extra_condition:
            setattr(
                instance,
                target_field,
                translate_to_language(getattr(instance, source_field), lang=to_lang),
            )
