from django.core.validators import MinValueValidator
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from embed_video.fields import EmbedVideoField

from hanbild.utils import set_translation_attrs


class Solution(models.Model):

    solution_title = models.CharField(
        max_length=250,
        verbose_name="Назва сервісу",
    )

    slug = models.SlugField(
        max_length=200,
        unique=True,
        null=True,
        verbose_name="URL",
    )

    index_on_page = models.IntegerField(
        verbose_name="Порядковий номер",
        validators=[MinValueValidator(0)],
        default=0,
    )

    review_content = models.TextField(verbose_name="Вступний текст")

    review_image = models.ImageField(
        upload_to="solution_images",
        verbose_name="Фото до вступного тексту",
    )

    content = CKEditor5Field(
        "Контент",
        null=True,
        blank=True,
        config_name="extends",
    )
    title = models.CharField(
        max_length=250,
        verbose_name="Назва сторінки",
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name="Опис для метатегу",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "solution"
        verbose_name = "послуга"
        verbose_name_plural = "Послуги"

    def save(self, *args, **kwargs):
        set_translation_attrs(self, ("solution_title", "review_content"))
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.solution_title}"


class SolutionPhotos(models.Model):
    solution = models.ForeignKey(
        to=Solution,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Послуга",
    )
    image = models.ImageField(
        upload_to="solution_images",
        verbose_name="Фото",
    )

    def __str__(self):
        return f"Фото для послуги: {self.solution}"

    class Meta:
        db_table = "solution_photo"
        verbose_name = "фото послуги"
        verbose_name_plural = "Фото послуги"


class SolutionVideos(models.Model):
    solution = models.ForeignKey(
        to=Solution,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Послуга",
    )
    video = EmbedVideoField(verbose_name="Посилання на відео")

    def __str__(self):
        return f"Відео для категорії: {self.solution}"

    class Meta:
        db_table = "solution_videos"
        verbose_name = "відео послуги"
        verbose_name_plural = "Відео послуги"
