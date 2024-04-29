from django.core.validators import MinValueValidator
from django.db import models

from vacancy.utils import translate_vacancy, translate_vacancy_description
from django.utils.translation import gettext_lazy as _


class Vacancy(models.Model):
    position = models.CharField(max_length=150, verbose_name="Назва вакансії")
    min_salary = models.IntegerField(
        verbose_name="Мінімальна зарплатня", validators=[MinValueValidator(0)]
    )
    max_salary = models.IntegerField(
        verbose_name="Максимальна зарплатня", validators=[MinValueValidator(0)]
    )

    def save(self, *args, **kwargs):
        translate_vacancy(self)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.position}"

    class Meta:
        db_table = "vacancies"
        verbose_name = "вакансія"
        verbose_name_plural = "Вакансії"


class VacancyDescription(models.Model):
    vacancy = models.ForeignKey(
        to=Vacancy(), on_delete=models.CASCADE, verbose_name="Вакансія"
    )
    CHOICES = (
        (1, _("Вимоги")),
        (2, _("Обов'язки")),
        (3, _("Умови")),
        (4, _("Від нас")),
    )

    choice = models.IntegerField(choices=CHOICES, verbose_name="Виберіть")
    text = models.TextField(verbose_name="Введіть інформацію")

    def save(self, *args, **kwargs):
        translate_vacancy_description(self)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Опис вакансії: {self.vacancy.position}"

    class Meta:
        db_table = "vacancies_description"
        verbose_name = "опис вакансії"
        verbose_name_plural = "Опис вакансій"
