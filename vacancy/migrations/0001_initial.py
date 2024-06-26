# Generated by Django 4.2.10 on 2024-04-17 15:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vacancy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "position",
                    models.CharField(max_length=150, verbose_name="Назва вакансії"),
                ),
                (
                    "position_uk",
                    models.CharField(
                        max_length=150, null=True, verbose_name="Назва вакансії"
                    ),
                ),
                (
                    "position_en",
                    models.CharField(
                        max_length=150, null=True, verbose_name="Назва вакансії"
                    ),
                ),
                (
                    "min_salary",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Мінімальна зарплатня",
                    ),
                ),
                (
                    "max_salary",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Максимальна зарплатня",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="VacancyDescription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "choice",
                    models.CharField(
                        choices=[
                            (1, "Вимоги"),
                            (2, "Обов'язки"),
                            (3, "Умови"),
                            (4, "Від нас"),
                        ],
                        max_length=20,
                        verbose_name="Виберіть",
                    ),
                ),
                (
                    "choice_uk",
                    models.CharField(
                        choices=[
                            (1, "Вимоги"),
                            (2, "Обов'язки"),
                            (3, "Умови"),
                            (4, "Від нас"),
                        ],
                        max_length=20,
                        null=True,
                        verbose_name="Виберіть",
                    ),
                ),
                (
                    "choice_en",
                    models.CharField(
                        choices=[
                            (1, "Вимоги"),
                            (2, "Обов'язки"),
                            (3, "Умови"),
                            (4, "Від нас"),
                        ],
                        max_length=20,
                        null=True,
                        verbose_name="Виберіть",
                    ),
                ),
                ("text", models.TextField(verbose_name="Введіть інформацію")),
                (
                    "text_uk",
                    models.TextField(null=True, verbose_name="Введіть інформацію"),
                ),
                (
                    "text_en",
                    models.TextField(null=True, verbose_name="Введіть інформацію"),
                ),
                (
                    "vacancy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vacancy.vacancy",
                        verbose_name="Вакансія",
                    ),
                ),
            ],
        ),
    ]
