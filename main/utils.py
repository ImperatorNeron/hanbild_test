import time
from django.http import JsonResponse

from main.models import ClientMessages
from main.sending_email_service import send_email
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def create_user_message(form, **kwargs):
    """
    Function needs to send user messages and write it in database.
    Return json response for interaction with ajax
    """
    ClientMessages.objects.create(
        name=form.cleaned_data["name"],
        number_or_email=form.cleaned_data["number_or_email"],
        message=form.cleaned_data["message"],
    )
    try:
        validate_email(form.cleaned_data["number_or_email"])
        # Messages for user
        form.cleaned_data["successful_message_1"] = f"Дякуємо за Ваше повідомлення!"
        form.cleaned_data["successful_message_2"] = (
            f"Найближчим часом з вами зв'яжеться наш менеджер."
        )
        send_email(
            form.cleaned_data,
            "email_letters/success_message.html",
            send_to=form.cleaned_data["number_or_email"],
        )
    except ValidationError:
        print("Введено номер телефону або неправильну адресу")

    # Messages for company
    form.cleaned_data["successful_message_1"] = (
        f"Нове повідомлення від '{form.cleaned_data['name']}'"
    )
    form.cleaned_data["successful_message_2"] = (
        f"Зв'яжіться з клієнтом за даними, які наведені нижче."
    )
    send_email(form.cleaned_data, "email_letters/success_message.html")
    return JsonResponse({"success": True, "message": "Повідомлення надійшло успішно!"})


def contact_form_errors(form, **kwargs):
    """
    Forms errors in json format
    """
    # For pretty preload view
    time.sleep(0.5)
    return JsonResponse({"success": False, "form_errors": form.errors})
