from django.db import models
from apps.clients.models import Client
from .choices import CURRENCIES


class Debt(models.Model):
    """Справа(Договір)"""

    class Meta:
        db_table = "debts"
        verbose_name = "Справа"
        verbose_name_plural = "Справи"

    # contract_sys_number = models.IntegerField(primary_key=True, verbose_name="Номер договору в системі")
    contract_origin_number = models.CharField(max_length=20, blank=False, null=False,
                                              verbose_name="Оригінальний номер договору")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клієнт")
    currency = models.CharField(max_length=4, choices=CURRENCIES, verbose_name="Валюта")
    commission = models.IntegerField(null=False, blank=False, verbose_name="Комісія")

    date_of_creation = models.DateField(null=False, blank=False, verbose_name="Дата заключення договору")
    end_date = models.DateField(null=False, blank=False, verbose_name="Дата закінчення договору")
    initial_amount = models.IntegerField(null=False, blank=False, verbose_name="Початкова сума")
    total_amount = models.IntegerField(null=False, blank=False, verbose_name="Загальна сума виданих коштів")
    current_debt = models.IntegerField(null=False, blank=False, verbose_name="Поточний борг")
    amount_of_payments = models.IntegerField(null=False, blank=False, verbose_name="Загальна сума виплат")
    last_payment_date = models.DateTimeField(null=True, blank=True, verbose_name="Дата останнього платежу")
    last_payment_amount = models.IntegerField(verbose_name="Сума останнього платежу")
    total_prolongation_amount = models.IntegerField(null=True, blank=True, verbose_name="Загальна сума пролонгацій")
    loan_body = models.IntegerField(null=True, blank=True, verbose_name="Тіло позики")
    loan_profit = models.IntegerField(null=True, blank=True, verbose_name="Проценти по позиці")
    penalty = models.IntegerField(null=True, blank=True, verbose_name="Пеня")
    fines = models.IntegerField(null=True, blank=True, verbose_name="Штрафи")
    delay_date = models.DateField(verbose_name="Дата виникнення просрочки")
    days_overdue = models.IntegerField(verbose_name="Кількість днів просрочки")
    credit_company = models.CharField(max_length=50, null=True, blank=True, verbose_name="Кредитна компанія")
    credit_brand = models.CharField(max_length=50, null=True, blank=True, verbose_name="Кредитний бренд")
    title_counterparty = models.CharField(max_length=50, null=True, blank=True, verbose_name="Назва контрагента")
    id_counterparty = models.CharField(max_length=50, null=True, blank=True, verbose_name="ID контрагента")

    def update(self):
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.id}, {self.contract_origin_number}, {self.total_amount}грн, {self.client}"