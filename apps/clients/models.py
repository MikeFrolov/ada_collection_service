from django.db import models
from django.utils import timezone
from apps.core.models import Person


class Client(Person):
    ipn = models.BigIntegerField(null=True, blank=True, verbose_name="ІПН")
    passport_serial = models.CharField(max_length=10, null=True, blank=True, verbose_name="Серія паспорту")
    passport_number = models.IntegerField(blank=True, verbose_name="Номер паспорту")
    addresses = models.JSONField(null=True, blank=True, verbose_name="Адреси")
    employer = models.CharField(max_length=255, null=True, blank=True, verbose_name="Роботодавець")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Дата внесення в реєстр")
    update_date = models.DateTimeField(blank=True, null=False, verbose_name="Дата оновлення")
    number_of_debts = models.IntegerField(null=True, blank=True, verbose_name="Кількість справ")
    comment = models.TextField()

    def update(self):
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}, ІПН: {self.ipn}, " \
               f"Кількість справ: {self.number_of_debts}"
