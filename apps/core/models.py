from django.db import models


class Person(models.Model):
    """Abstract class for all models Human"""

    last_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Прізвище"
    )
    first_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Ім'я"
    )
    patronymic = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="По-батькові"
    )

    class Meta:
        abstract = True
