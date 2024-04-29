from django import forms
from django.core.validators import EmailValidator, RegexValidator
from django.utils.translation import gettext_lazy as _

class CreateOrderForm(forms.Form):

    ukr_eng_alpha_validator = RegexValidator(
        regex=r"^[a-zA-Zа-яА-ЯіІїЇєЄґҐ.,\s`\'’-]+$",
        message=_("Поле не може містити цифри та заборонені знаки!"),
        code="invalid_characters",
    )

    name = forms.CharField(validators=[ukr_eng_alpha_validator])
    surname = forms.CharField(validators=[ukr_eng_alpha_validator])
    phone_number = forms.CharField(
        validators=[
            RegexValidator(
                regex="^\+?1?\d{9,15}$",
                message=_("Номер телефону повинен бути в форматі +380960001122 або 0960001122"),
                code="invalid_phone_number",
            )
        ]
    )
    email = forms.CharField(
        validators=[
            EmailValidator(
                message=_("Введіть коректну електронну пошту"), code="invalid_email"
            )
        ]
    )
    city = forms.CharField(validators=[ukr_eng_alpha_validator])
    delivery_address = forms.CharField(
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z0-9а-яА-ЯіІїЇєЄґҐ.,\s`'’\-/\\]+$",
                message=_("Адреса не може містити заборонені знаки!"),
                code="invalid_address_characters",
            )
        ]
    )
    message = forms.CharField(widget=forms.Textarea, required=False)
