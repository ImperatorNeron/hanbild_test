from deep_translator import GoogleTranslator


def translate_to_en(to_field):
    """
    Translate field into English
    :param to_field: text in Ukrainian
    :return: translated text or None
    """
    try:
        return GoogleTranslator(source="auto", target="en").translate(to_field)
    except Exception as e:
        print(f"Translation failed: {e}")


def translate_vacancy(instance):
    """
    Translate vacancy position to English if not already translated
    :param instance: Vacancy instance
    """
    if not instance.position_en:
        instance.position_en = translate_to_en(instance.position_uk)


def translate_vacancy_description(instance):
    """
    Translate vacancy description to English if not already translated
    :param instance: Vacancy instance
    """
    if not instance.text_en:
        instance.text_en = translate_to_en(instance.text_uk)
