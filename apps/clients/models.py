from django.db import models
from django.utils import timezone
from datetime import datetime

from apps.core.models import Person


class Client(Person):
    """Клієнт(Боржник)"""

    # Gender choices
    class GenderChoices(models.TextChoices):
        F = 'Жін', 'Жіноча'
        M = 'Чол', 'Чоловіча'
        O = 'Інше', 'Інше'

    gender = models.CharField(
        max_length=4,
        choices=GenderChoices.choices,
        verbose_name="Стать"
    )
    date_of_birth = models.DateField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True,
        verbose_name="Дата народження"
    )
    ipn = models.BigIntegerField(null=True, blank=True, unique=True, verbose_name="ІПН")
    passport_serial = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="Серія паспорту"
    )
    passport_number = models.IntegerField(null=True, blank=True, verbose_name="Номер паспорту")
    employer = models.CharField(max_length=255, null=True, blank=True, verbose_name="Роботодавець")
    position = models.CharField(max_length=128, null=True, blank=True, verbose_name="Посада")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Дата внесення в реєстр")
    update_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата оновлення")

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
        verbose_name="Клієнт",
        primary_key=True
    )
    military = models.BooleanField(default=False, verbose_name='Військовий')
    displaced = models.BooleanField(default=False, verbose_name='Тимчасово переміщений')
    abroad = models.BooleanField(default=False, verbose_name='Виїхав за кордон')
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


class ClientSocialNetworks(models.Model):
    """Соціальні мережі клієнта"""
    client = models.OneToOneField(
        Client,
        unique=True,
        on_delete=models.CASCADE,
        verbose_name="Клієнт",
        primary_key=True
    )
    facebook = models.URLField(max_length=128, blank=True, verbose_name="Facebook")
    linkedin = models.URLField(max_length=128, blank=True, verbose_name="LinkedIn")
    instagram = models.URLField(max_length=128, blank=True, verbose_name="Instagram")
    tictok = models.URLField(max_length=128, blank=True, verbose_name="Tik Tok")

    class Meta:
        db_table = "client_social_networks"
        verbose_name = "Соціальні мережі клієнта"
        verbose_name_plural = "Соціальні мережі клієнтів"

    def __str__(self):
        return f"Соціальні мережі клієтна: {self.client}"


class ClientContactPerson(Person):
    """Persons related to the client (relatives, acquaintances, guarantors)"""
    client = models.ForeignKey(
        Client,
        on_delete=models.RESTRICT,
        verbose_name="Клієнт"
    )

    # Relations with client
    class RelationChoices(models.TextChoices):
        CR = "Близькі родичі", "Близькі родичі"
        DR = "Далекі родичі", ""
        FR = "Друзі", "Друзі"
        CL = "Коллеги", "Коллеги"
        NG = "Сусіди", "Сусіди"
        GR = "Поручитель", "Поручитель"
        MR = "Заставодавець", "Заставодавець"

    relations = models.CharField(max_length=14, choices=RelationChoices.choices, verbose_name='Тип звязку')
    priority = models.BooleanField(default=False, verbose_name='Основний контакт')

    class Meta:
        db_table = "clients_contacts_persons"
        verbose_name = "Повязана особа"
        verbose_name_plural = "Повязані особи"
        unique_together = (('client', 'last_name', 'first_name', 'patronymic'),)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"
