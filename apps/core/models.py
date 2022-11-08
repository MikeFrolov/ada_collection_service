from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
    """Abstract class for all models Human"""

    class GenderChoices(models.TextChoices):
        FEMALE = 'Жіноча', 'Жіноча'
        MALE = 'Чоловіча', 'Чоловіча'
        NOT_INDICATED = 'Не вказана', 'Не вказана'

    last_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Прізвище"
    )
    first_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="Ім'я"
    )
    patronymic = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="По-батькові"
    )
    date_of_birth = models.DateField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True,
        verbose_name="Дата народження"
    )
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
        default=GenderChoices.NOT_INDICATED,
    )
    primary_phone_number = PhoneNumberField(
        null=True,
        blank=False,
        unique=True,
        verbose_name="Основний номер телефону"
    )
    additional_phone_number = PhoneNumberField(
        null=True,
        blank=True,
        unique=False,
        verbose_name="Додатковий номер телефону"
    )
    work_phone_number = PhoneNumberField(
        null=True,
        blank=True,
        unique=False,
        verbose_name="Робочий номер телефону"
    )
    home_phone_number = PhoneNumberField(
        null=True,
        blank=True,
        unique=False,
        verbose_name="Домашній номер телефону"
    )
    email = models.EmailField(
        max_length=255,
        verbose_name="Електронна пошта"
    )

    class Meta:
        abstract = True
