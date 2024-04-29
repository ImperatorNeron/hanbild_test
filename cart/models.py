from django.db import models
from catalog.models import Goods


class CartQueryset(models.QuerySet):
    def total_price(self):
        if self:
            return sum(cart.goods_price() for cart in self)
        return 0

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    item = models.ForeignKey(to=Goods, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Кількість")
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата додадання"
    )
    session_key = models.CharField(max_length=32, null=True, blank=True)

    class Meta:
        db_table = "cart"
        verbose_name = "корзину"
        verbose_name_plural = "Корзина"

    objects = CartQueryset().as_manager()

    def __str__(self) -> str:
        return f"Товар: {self.item.name} | Кількість: {self.quantity}"

    def goods_price(self):
        return self.item.price * self.quantity
