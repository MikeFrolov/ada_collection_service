from django.db import models
from apps.clients.models import Client
from apps.contractors.models import Contractor
from apps.contractor_managers.models import ContractorManager


class Address(models.Model):
    """Адреса"""
    class AddressTypeChoices(models.TextChoices):
        COMPANY = 'Company address', 'Адреса компанії'
        LEGAL = 'Legal address', 'Адреса реєстрації'
        PHYSICAL = 'Physical address', 'Адреса проживання'
        WORK = 'Work address', 'Адреса працевлаштування'

    class ApartmentTypeChoices(models.TextChoices):
        APARTMENT = 'кв.', 'Квартира'
        OFFICE = 'оф.', 'Офіс'

    class CityTypeChoices(models.TextChoices):
        V = 'с.', 'Село'
        C = 'м.', 'Місто'
        UV = 'смт.', 'Селище міського типу'

    class StreetTypeChoices(models.TextChoices):
        PROSP = 'просп.', 'Проспект'
        VUL = 'вул.', 'Вулиця'
        PROV = 'пров.', 'Провулок'
        BULV = 'б-р.', 'Бульвар'
        NAB = 'наб.', 'Набережна'
        TUP = 'туп.', 'Тупик'

    person = None
    type_address = models.CharField(
        max_length=16,
        default=AddressTypeChoices.LEGAL,
        choices=AddressTypeChoices.choices,
        blank=True,
        verbose_name="Тип адреси"
    )
    index = models.CharField(max_length=8, blank=True, verbose_name="Індекс")
    country = models.CharField(max_length=50, blank=False, default='Україна', verbose_name="Країна")
    province = models.CharField(max_length=50, blank=False, verbose_name="Область")
    district = models.CharField(max_length=50, blank=True, verbose_name="Район")
    type_city = models.CharField(
        max_length=4,
        default=CityTypeChoices.C,
        choices=CityTypeChoices.choices,
        blank=False,
        verbose_name="Тип населеного пункту"
    )
    city = models.CharField(max_length=50, blank=False, verbose_name="Місто")
    city_district = models.CharField(max_length=50, blank=True, verbose_name="Район-міста")
    type_street = models.CharField(
        max_length=6,
        default=StreetTypeChoices.VUL,
        choices=StreetTypeChoices.choices,
        blank=False,
        verbose_name="Тип вулиці"
    )
    street = models.CharField(max_length=50, blank=False, verbose_name="Вулиця")
    house = models.CharField(max_length=9, blank=False, verbose_name="Будинок")
    apartment_type = models.CharField(
        max_length=9,
        choices=ApartmentTypeChoices.choices,
        blank=True,
        verbose_name="Тип приміщення"
    )
    apartment_number = models.CharField(max_length=6, blank=True, verbose_name="Номер приміщення")

    class Meta:
        abstract = True


class ClientAddress(Address):
    """Адреса клієнта"""
    person = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клієнт")

    class Meta:
        db_table = "client_address"
        verbose_name = "Адреса клієнта"
        verbose_name_plural = "Адреси клієнтів"
        unique_together = (('person', 'type_address'),)

    def __str__(self):
        return f"{self.country}, {self.index}, {self.province} обл., {self.district} р-н., {self.type_city}" \
               f"{self.city}, {self.type_street} {self.street}, буд. {self.house}," \
               f" {self.apartment_type}{self.apartment_number}"


class ContractorAddress(Address):
    """Адреса контрагента"""
    person = models.ForeignKey(Contractor, on_delete=models.CASCADE, verbose_name="Контрагент")

    class Meta:
        db_table = "contractor_address"
        verbose_name = "Адреса контрагента"
        verbose_name_plural = "Адреси контрагентів"
        unique_together = (('person', 'type_address'),)

    def __str__(self):
        return f"{self.person}: {self.country}, {self.index}, {self.province} обл., {self.district} р-н., {self.type_city}" \
               f"{self.city}, {self.type_street}{self.street}, буд.{self.house}," \
               f" {self.apartment_type}{self.apartment_number}"


class ContractorManagerAddress(Address):
    """Адреса менеджера контрагента"""
    person = models.ForeignKey(ContractorManager, on_delete=models.CASCADE, verbose_name="Менеджер контрагента")

    class Meta:
        db_table = "contractor_manager_address"
        verbose_name = "Адреса менеджера контрагента"
        verbose_name_plural = "Адреси менеджерів контрагентів"
        unique_together = (('person', 'type_address'),)

    def __str__(self):
        return f"{self.person}: {self.country}, {self.index}, {self.province} обл., {self.district} р-н., {self.type_city}" \
               f"{self.city}, {self.type_street}{self.street}, буд.{self.house}," \
               f" {self.apartment_type}{self.apartment_number}"
