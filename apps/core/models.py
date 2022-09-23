from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
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

