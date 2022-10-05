from django.db import models
from django.utils import timezone
from datetime import datetime

from apps.core.models import Person


class Client(Person):
    """Клієнт(Боржник)"""

    class Meta:
        db_table = "clients"
        verbose_name = "Клієнт"
        verbose_name_plural = "Клієнти"

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

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    def save(self, *args, **kwargs):
        self.last_updated_dt = datetime.now()
        super().save(*args, **kwargs)