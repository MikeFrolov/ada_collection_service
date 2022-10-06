from django.db import models
from django.utils import timezone
from apps.clients.models import Client
from apps.contractors.models import Contractor
from apps.contractor_managers.models import ContractorManager


class Debt(models.Model):
    """Справа(Договір)"""
    class CurrencyChoices(models.TextChoices):
        USD = 'USD', 'US Dollar',
        EUR = 'EUR', 'Euro',
        UAH = 'UAH', 'Гривня',

    origin_number = models.CharField(
        max_length=15,
        blank=False,
        null=False,
        unique=False,
        verbose_name="Оригінальний номер договору"
    )
    number_from_contractor = models.CharField(
        max_length=15,
        blank=False,
        null=False,
        unique=False,
        verbose_name="Номер договору в системі контрагента"
    )
    client = models.ForeignKey(Client, on_delete=models.RESTRICT, verbose_name="Клієнт")
    date_of_creation = models.DateField(
        null=False,
        blank=False,
        verbose_name="Дата заключення договору",
        help_text='format: 01.01.2000'
    )
    end_date = models.DateField(null=False, blank=False, verbose_name="Дата закінчення договору")
    # fixme: Створити модель кредитної компанії "meny to many з брендом"
    credit_company = models.CharField(max_length=50, null=True, blank=True, verbose_name="Кредитна компанія")
    # fixme: Створити модель кредитного бренду
    credit_brand = models.CharField(max_length=50, null=True, blank=True, verbose_name="Кредитний бренд")
    title_contractor = models.ForeignKey(Contractor, on_delete=models.RESTRICT, verbose_name="Назва контрагента")
    # fixme: contractor_manager має вибиратися зі списку менеджерів саме одного контрагента
    # contractor_manager = (verbose_name="Менеджер контрагента")
    payment_amounts = models.IntegerField(null=False, blank=False, default=0, verbose_name="Кількість платежів")
    number_of_late_payments = models.IntegerField(null=False, blank=False, default=0, verbose_name="Кількість прострочених платежів")
    monthly_payment_amount = models.FloatField(null=False, blank=False, default=0, verbose_name="Сума щомісячного платежу")
    initial_amount = models.FloatField(null=False, blank=False, default=0, verbose_name="Початкова сума")
    total_issued_amount = models.FloatField(null=False, blank=False, default=0, verbose_name="Загальна сума виданих коштів")
    amount_of_payments = models.IntegerField(null=False, blank=False, default=0, verbose_name="Загальна сума виплат")
    principal = models.FloatField(null=True, blank=True, default=0, verbose_name="Основний борг")
    commission = models.FloatField(null=False, blank=False, default=0, verbose_name="Комісії")
    interest = models.FloatField(null=True, blank=True, default=0, verbose_name="Відсотки")
    penalty = models.FloatField(null=True, blank=True, default=0, verbose_name="Пеня")
    fines = models.FloatField(null=True, blank=True, default=0, verbose_name="Штрафи")
    current_debt = models.FloatField(null=False, blank=False, default=0, verbose_name="Поточний борг")
    total_prolongation_amount = models.FloatField(null=True, blank=True, default=0, verbose_name="Загальна сума пролонгацій")
    last_payment_date = models.DateTimeField(null=True, blank=True, verbose_name="Дата останнього платежу")
    last_payment_amount = models.FloatField(max_length=8, null=True, blank=True, default=0, verbose_name="Сума останнього платежу")
    currency = models.CharField(
        max_length=3,
        default=CurrencyChoices.UAH,
        choices=CurrencyChoices.choices,
        verbose_name="Валюта"
    )
    delay_date = models.DateField(verbose_name="Дата виникнення просрочки")
    delay_days = models.IntegerField(null=True, blank=True, default=0, verbose_name="Кількість днів просрочки")

    class Meta :
        db_table = "debt"
        verbose_name = "Справа"
        verbose_name_plural = "Справи"

    def update(self):
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.id}, {self.origin_number}, {self.current_debt}грн, {self.client}"
