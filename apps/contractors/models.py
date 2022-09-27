from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .choices import TYPE_CONTRACTOR
from apps.core.models import Person


class Contractor(models.Model):
    """Контрагент(Організація що надає справи)"""

    class Meta:
        db_table = "contractor"
        verbose_name = "Контрагент"
        verbose_name_plural = "Контрагенти"

    type = models.CharField(max_length=4, choices=TYPE_CONTRACTOR, verbose_name="Тип контрагента")
    edrpou = models.IntegerField(null=False, blank=False, verbose_name="ЄДРПОУ")
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Назва компанії")
    email = models.EmailField(max_length=255, verbose_name="Електронна пошта")
    phone = PhoneNumberField(null=True, blank=False, unique=True, verbose_name="Номер телефону")
    address = models.JSONField(blank=True, verbose_name="Адреса")
    post_address = models.JSONField(blank=True, verbose_name="Поштова адреса")

    def __str__(self):
        return f"{self.title}"


class Manager(Person):
    position = models.CharField(max_length=50, null=False, blank=False, verbose_name="Посада")
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, verbose_name="Контрагент")
