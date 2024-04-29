from django.core.mail import EmailMessage
from django.forms import ValidationError
from django.template.loader import render_to_string


def send_email(context, letter_template, send_to="www.vladik49@gmail.com"):
    """
    Function for message sending
    :context: parameters from forms or custom messages for user and company
    :letter_template: html page for email letter
    """
    try:
        html_content = render_to_string(
            letter_template,
            context=context,
        )

        # save message to db
        email = EmailMessage(
            subject=f"Повідомлення від Hanbild",
            body=html_content,
            from_email="km2022tm@gmail.com",
            to=[send_to],
        )
        email.content_subtype = "html"
        email.send()
    except ValidationError as e:
        print(f"Validation Error: {e}")
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")
