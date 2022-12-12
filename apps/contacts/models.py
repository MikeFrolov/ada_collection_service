from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.clients.models import Client, ClientContactPerson
from apps.core.choices import VerificationChoices


class PhoneNumber(models.Model):
    phone = PhoneNumberField(
        null=True,
        blank=True,
        verbose_name="Номер телефону"
    )

    # Typification
    class TypePhoneChoices(models.TextChoices):
        M = "Моб.", "Мобільний"
        H = "Дом.", "Домашній"
        W = "Роб.", "Робочий"
        A = "Додат.", "Додатковий"

    type_phone = models.CharField(max_length=6,
                                  choices=TypePhoneChoices.choices,
                                  default=TypePhoneChoices.M,
                                  verbose_name='Тип номеру телефону'
                                  )

    # Verification
    verification = models.CharField(max_length=3,
                                    null=True,
                                    blank=True,
                                    choices=VerificationChoices.choices,
                                    verbose_name='Верифікація'
                                    )
    # Messengers
    facetime = models.BooleanField(default=False, verbose_name='FaceTime')
    signal = models.BooleanField(default=False, verbose_name='Signal')
    telegram = models.BooleanField(default=False, verbose_name='Telegram')
    viber = models.BooleanField(default=False, verbose_name='Viber')
    whatsapp = models.BooleanField(default=False, verbose_name='WhatsApp')
    olx = models.BooleanField(default=False, verbose_name='OLX')
    prom = models.BooleanField(default=False, verbose_name='Prom.ua')

    class Meta:
        abstract = True


class ClientPhone(PhoneNumber):
    """Client phone number"""
    # TODO: Додати поле 'Основний номер' (основний вивести першим, якщо їх більше я 1 - то по даті (по убуванню))
    client = models.ForeignKey(Client, on_delete=models.RESTRICT, verbose_name="Клієнт")

    class Meta:
        db_table = "clients_phones"
        verbose_name = "Номер телефону клієнта"
        verbose_name_plural = "Номери телефонів клієнтів"
        unique_together = (('client', 'phone'), ('client', 'type_phone'))

    def __str__(self):
        return f"{self.phone}"


class ClientContactPersonPhone(PhoneNumber):
    contact_person = models.ForeignKey(
        ClientContactPerson,
        on_delete=models.CASCADE,
        verbose_name="Контактне лице"
    )

    class Meta:
        db_table = "client_contact_persons_phones"
        verbose_name = "Телефон контактної особи клієнта"
        verbose_name_plural = "Телефони контактних осіб клієнтів"
        unique_together = (
            ('contact_person', 'phone'),
            ('contact_person', 'phone', 'verification'),
            ('contact_person', 'type_phone')
        )

    def __str__(self):
        return f"{self.phone}"


class EmailAddress(models.Model):
    """Email address model"""
    email = models.EmailField(
        max_length=255,
        verbose_name="Електронна пошта"
    )

    # Verification
    verification = models.CharField(max_length=3,
                                    null=True,
                                    blank=True,
                                    choices=VerificationChoices.choices,
                                    verbose_name='Верифікація'
                                    )

    class Meta:
        abstract = True


class ClientEmail(EmailAddress):
    """Client email address"""
    client = models.ForeignKey(Client, on_delete=models.RESTRICT, verbose_name="Клієнт")

    class Meta:
        db_table = "client_email"
        verbose_name = "Електронна пошта клієнта"
        verbose_name_plural = "Електронні пошти клієнта"
        unique_together = (('client', 'email'),)

    def __str__(self):
        return f"{self.email}"


class ClientContactPersonEmail(EmailAddress):
    """Client contact person email address"""
    contact_person = models.ForeignKey(ClientContactPerson, on_delete=models.CASCADE, verbose_name="Контактне лице")

    class Meta:
        db_table = "client_contact_persons_emails"
        verbose_name = "Електронна пошта контактної особи клієнта"
        verbose_name_plural = "Електронні пошти контактних осіб клієнтів"
        unique_together = (('contact_person', 'email'),)
