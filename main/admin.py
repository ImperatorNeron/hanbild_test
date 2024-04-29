from django.contrib import admin

from main.models import ClientMessages


@admin.register(ClientMessages)
class ClientMessagesAdmin(admin.ModelAdmin): 
    list_display = ("name", "number_or_email", "message", "send_message_time")
    list_display_links = ("name", "number_or_email")
    list_filter = ("send_message_time", )

