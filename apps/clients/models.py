from django.db import models
from django.utils import timezone
from datetime import datetime

from apps.core.models import Person


class Client(Person):
    """Клієнт(Боржник)"""

    ipn = models.BigIntegerField(null=True, blank=True, unique=True, verbose_name="ІПН")
    passport_serial = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="Серія паспорту"
    )
    passport_number = models.IntegerField(null=True, blank=True, verbose_name="Номер паспорту")
    addresses = models.JSONField(null=True, blank=True, verbose_name="Адреси")
    employer = models.CharField(max_length=255, null=True, blank=True, verbose_name="Роботодавець")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Дата внесення в реєстр")
    update_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата оновлення")
    # number_of_debts = models.IntegerField(null=True, blank=True, verbose_name="Кількість справ")
    comment = models.TextField(blank=True, verbose_name="Коментар")

    # def update(self):
    #     self.update_date = timezone.now()
    #     self.save()

    class Meta:
        db_table = "clients"
        verbose_name = "Клієнт"
        verbose_name_plural = "Клієнти"
        unique_together = (('passport_serial', 'passport_number'),)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    def save(self, *args, **kwargs):
        self.last_updated_dt = datetime.now()
        super().save(*args, **kwargs)


class ClientStatuses(models.Model):
    """Статуси клієнта"""
    client = models.OneToOneField(
        Client,
        unique=True,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="Клієнт"
    )
    military = models.BooleanField(default=False, verbose_name='Військовий')
    displaced = models.BooleanField(default=False, verbose_name='Тимчасово переміщений')
    abroad = models.BooleanField(default=False, verbose_name='Віїхав за кордон')
    occupation = models.BooleanField(default=False, verbose_name='Під окупацією')
    credited = models.BooleanField(default=False, verbose_name='Закредитований')
    bankrupt = models.BooleanField(default=False, verbose_name='Банкрот')
    imprisoned = models.BooleanField(default=False, verbose_name='Тюрма')
    illness = models.BooleanField(default=False, verbose_name='Хвороба')
    death = models.BooleanField(default=False, verbose_name='Смерть')

    class Meta:
        db_table = "client_statuses"
        verbose_name = "Статуси клієнта"
        verbose_name_plural = "Статуси клієнтів"

    def __str__(self):
        return f"Статуси клієтна: {self.client}"
