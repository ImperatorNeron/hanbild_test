from django.db import models

from catalog.models import Goods


class OrderDetails(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ім'я")
    surname = models.CharField(max_length=50, verbose_name="Прізвище")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефону")
    email = models.CharField(max_length=70, verbose_name="Email")
    city = models.CharField(max_length=30, verbose_name="Місто")
    delivery_address = models.CharField(max_length=100, verbose_name="Адреса доставки")
    message = models.TextField(verbose_name="Повідомлення", null=True, blank=True)
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата створення замовлення"
    )
    status = models.CharField(
        max_length=50, default="В обробці", verbose_name="Статус замовлення"
    )

    class Meta:
        db_table = "order"
        verbose_name = "замовлення"
        verbose_name_plural = "Замовлення"

    def __str__(self):
        return f"Замовлення № {self.pk} | Покупець {self.name} {self.surname}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        to=OrderDetails, on_delete=models.CASCADE, verbose_name="Замовлення"
    )
    product = models.ForeignKey(
        to=Goods,
        on_delete=models.SET_DEFAULT,
        null=True,
        verbose_name="Товар",
        default=None,
    )
    name = models.CharField(max_length=150, verbose_name="Назва")
    price = models.FloatField(verbose_name="Ціна")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Кількість")
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата продажі"
    )

    class Meta:
        db_table = "order_item"
        verbose_name = "Проданий товар"
        verbose_name_plural = "Продані товари"

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f"Замовлення № {self.order.pk} | Товар: {self.name}"
