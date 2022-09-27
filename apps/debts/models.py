from django.db import models

from .choices import CURRENCIES, TYPE_CONTRACTOR
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from datetime import datetime


class Person(models.Model):
    """Abstract class for all models Human"""
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


class Client(Person):
    """Клієнт(Боржник)"""

    class Meta:
        db_table = "clients"
        verbose_name = "Клієнт"
        verbose_name_plural = "Клієнти"

    ipn = models.BigIntegerField(null=True, blank=True, verbose_name="ІПН")
    passport_serial = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="Серія паспорту"
    )
    passport_number = models.IntegerField(blank=True, verbose_name="Номер паспорту")
    addresses = models.JSONField(null=True, blank=True, verbose_name="Адреси")
    employer = models.CharField(max_length=255, null=True, blank=True, verbose_name="Роботодавець")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Дата внесення в реєстр")
    update_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата оновлення")
    # number_of_debts = models.IntegerField(null=True, blank=True, verbose_name="Кількість справ")
    comment = models.TextField()

    # def update(self):
    #     self.update_date = timezone.now()
    #     self.save()

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}, ІПН: {self.ipn}"

    def save(self, *args, **kwargs):
        self.last_updated_dt = datetime.now()
        super().save(*args, **kwargs)


class Contractor(models.Model):
    """Контрагент(Організація що надає справу)"""

    class Meta:
        db_table = "contractor"
        verbose_name = "Контрагент"
        verbose_name_plural = "Контрагенти"

    type = models.CharField(max_length=4, choices=TYPE_CONTRACTOR, verbose_name="Тип контрагента")
    edrpou = models.IntegerField(null=False, blank=False, verbose_name="ЄДРПОУ")
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Назва компанії")
    email = models.EmailField(max_length=255, verbose_name="Електронна пошта")
    phone = PhoneNumberField(null=True, blank=False, unique=True, verbose_name="Номер телефону")
    address = models.JSONField(null=True, blank=True, verbose_name="Адреса")
    post_address = models.JSONField(null=True, blank=True, verbose_name="Поштова адреса")

    def __str__(self):
        return f"{self.title}, {self.type}"


class ContractorManager(Person):
    """Менеджер контрагента(Менеджер організації що надає справу)"""
    class Meta:
        db_table = "сontractor_manager"
        verbose_name = "Менеджер контрагента"
        verbose_name_plural = "Менеджери контрагентів"

    position = models.CharField(max_length=50, null=False, blank=False, verbose_name="Посада")
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, verbose_name="Контрагент")

    def __str__(self):
        return f"{self.id}, {self.last_name} {self.first_name}, {self.contractor}"


class Debt(models.Model):
    """Справа(Договір)"""

    class Meta:
        db_table = "debt"
        verbose_name = "Справа"
        verbose_name_plural = "Справи"

    # contract_sys_number = models.IntegerField(primary_key=True, verbose_name="Номер договору в системі")
    contract_origin_number = models.CharField(max_length=20, blank=False, null=False,
                                              verbose_name="Оригінальний номер договору")
    client = models.ForeignKey(Client, on_delete=models.RESTRICT, verbose_name="Клієнт")
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
    title_contractor = models.ForeignKey(Contractor, on_delete=models.RESTRICT, verbose_name="Назва контрагента")
    # contractor_manager = models.ForeignKey(
    #     ContractorManager,
    #     on_delete=models.RESTRICT,
    #     verbose_name="Менеджер контрагента"
    # )

    def update(self):
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.id}, {self.contract_origin_number}, {self.current_debt}грн, {self.client}"
