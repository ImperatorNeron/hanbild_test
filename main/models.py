from django.db import models


class ClientMessages(models.Model):
    name = models.CharField(max_length=150, verbose_name="Ім'я", null=True, blank=True, default="Ім'я не вказано")
    number_or_email = models.CharField(max_length=200, verbose_name="Номер або email")
    message = models.TextField(verbose_name="Повідомлення", null=True, blank=True, default="Повідомлення не вказано")
    send_message_time = models.DateTimeField(auto_now_add=True, verbose_name="Дата повідомлення")

    def __str__(self):
        return f"{self.name} - {self.number_or_email}"

    class Meta:
        db_table = "client_message"
        verbose_name = "повідомлення клієнта"
        verbose_name_plural = "Повідомлення клієнтів"
