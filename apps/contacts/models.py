from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.clients.models import Client, ClientContactPerson


class PhoneNumber(models.Model):
    phone = PhoneNumberField(
        null=True,
        blank=True,
        verbose_name="Номер телефону"
    )

    # Typification
    class TypePhoneChoices(models.TextChoices):
        M = "Моб", "Мобільний"
        H = "Дом", "Домашній"
        W = "Роб", "Робочий"
        A = "Дод", "Додатковий"

    type_phone = models.CharField(max_length=3,
                                  choices=TypePhoneChoices.choices,
                                  default=TypePhoneChoices.M,
                                  verbose_name='Тип номеру телефону'
                                  )

    # Verification
    class VerificationChoices(models.TextChoices):
        BASE = "Осн", "Основний"
        ACT = "Акт", "Активний"
        PASS = "Пас", "Пасивний"

    verification = models.CharField(max_length=8,
                                    choices=VerificationChoices.choices,
                                    default=VerificationChoices.ACT,
                                    verbose_name='Верифікація'
                                    )
    # Messengers
    facetime = models.BooleanField(default=False, verbose_name='FaceTime')
    signal = models.BooleanField(default=False, verbose_name='Signal')
    telegram = models.BooleanField(default=False, verbose_name='Telegram')
    viber = models.BooleanField(default=False, verbose_name='Viber')
    whatsapp = models.BooleanField(default=False, verbose_name='WhatsApp')

    class Meta:
        abstract = True


class ClientPhone(PhoneNumber):
    """Client phone number"""
    client = models.ForeignKey(Client, on_delete=models.RESTRICT, verbose_name="Клієнт")

    class Meta:
        db_table = "clients_phones"
        verbose_name = "Номер телефону клієнта"
        verbose_name_plural = "Номери телефонів клієнтів"
        unique_together = (('client', 'phone'), ('client', 'phone', 'verification'), ('client', 'type_phone'))

    def __str__(self):
        return f"{self.phone}"


class ClientContactPersonPhone(PhoneNumber):
    сontact_person = models.ForeignKey(
        ClientContactPerson,
        on_delete=models.CASCADE,
        verbose_name="Контактне лице"
    )

    class Meta:
        db_table = "client_contact_persons_phones"
        verbose_name = "Телефон контактного лиця клієнта"
        verbose_name_plural = "Телефони контактних лиць клієнтів"
        unique_together = (
            ('сontact_person', 'phone'),
            ('сontact_person', 'phone', 'verification'),
            ('сontact_person', 'type_phone')
        )

    def __str__(self):
        return f"{self.phone}"


class ClientEmail(models.Model):
    """Client email address"""
    client = models.ForeignKey(Client, on_delete=models.RESTRICT, verbose_name="Клієнт")
    email = models.EmailField(
        max_length=255,
        verbose_name="Електронна пошта"
    )

    class Meta:
        db_table = "client_email"
        verbose_name = "Електронна пошта клієнта"
        verbose_name_plural = "Електронні пошти клієнта"
        unique_together = (('client', 'email'),)

    def __str__(self):
        return f"{self.email}"