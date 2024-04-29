from django.contrib import admin

from order.models import OrderDetails, OrderItem


class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = "product", "price", "quantity"
    readonly_fields = "product", "price", "quantity"
    search_fields = ("product",)
    extra = 0
    can_delete = False


@admin.register(OrderDetails)
class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "surname",
        "name",
        "phone_number",
        "email",
        "city",
        "delivery_address",
        "created_timestamp",
    )
    list_display_links = (
        "id",
        "surname",
        "name",
        "phone_number",
        "email",
        "city",
        "delivery_address",
    )
    fields = (
        ("surname", "name"),
        ("phone_number", "email"),
        ("city", "delivery_address"),
        "created_timestamp",
        "status",
        "message",
    )
    readonly_fields = ("created_timestamp",)

    search_fields = (
        "surname",
        "name",
        "phone_number",
        "email",
        "city",
        "delivery_address",
    )

    inlines = (OrderItemTabulareAdmin,)
    list_filter = ("created_timestamp", "status")