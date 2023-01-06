from django.db import models
from django.utils import timezone
from apps.clients.models import Client, ClientContactPerson
from .choices import INSTRUMENT_CHOICES, COMMUNICATION_CHANNEL_CHOICES, COMMUNICATION_RESULT_CHOICES, TYPE_COMMUNICATION_CHOICES
from apps.debts.models import Debt


class Communication(models.Model):
    """Communication model"""
    debt = models.ForeignKey(Debt, on_delete=models.RESTRICT, verbose_name="Справа", related_name='communications')
    date_time = models.DateTimeField(default=timezone.now)
    type = models.CharField(
        max_length=3,
        choices=TYPE_COMMUNICATION_CHOICES,
        verbose_name='Тип комунікації'
    )
    action = models.CharField(max_length=12, choices=INSTRUMENT_CHOICES, verbose_name='Дія')
    communication_channel = models.CharField(
        max_length=16,
        choices=COMMUNICATION_CHANNEL_CHOICES,
        verbose_name='Канал звязку'
    )
    communication_detail = models.CharField(max_length=100, verbose_name='Деталі')
    person = models.CharField(max_length=255, default='Клієнт', verbose_name='Контактна особа')
    result = models.CharField(max_length=4, choices=COMMUNICATION_RESULT_CHOICES, verbose_name='Результат')
    sum = models.IntegerField(null=True, blank=True, verbose_name="Обіцяна сума погашення")
    pay_date = models.DateField(null=True, blank=True, verbose_name="Обіцяна дата погашення")
    comment = models.TextField(verbose_name="Коментар/Текст")

    class Meta:
        db_table = "communications"
        verbose_name = "Комунікація"
        verbose_name_plural = "Комунікації"

    def __str__(self):
        return f"{self.debt} {self.date_time} {self.type} {self.action} {self.communication_channel} "
