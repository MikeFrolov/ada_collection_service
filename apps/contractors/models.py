from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contractor(models.Model):
    """Контрагент(Організація що надає справу)"""
    class ContractorTypeChoices(models.TextChoices):
        MFO = 'МФО', 'Мікрофінансова організація',
        FK = 'ФК', 'Факторингова компанія',
        BU = 'БАНК', 'Банкова установа',
        SK = 'СК', 'Страхова компанія',
        TK = 'ТК', 'Телекомунікаційна компанія',
        JKG = 'ЖКГ', 'Житлово-комунальне гопподарство'
        FGV = 'ФГВ', 'Фонд гарантування вкладів'

    type = models.CharField(
        max_length=4,
        default=ContractorTypeChoices.MFO,
        choices=ContractorTypeChoices.choices,
        verbose_name="Тип контрагента"
    )
    edrpou = models.IntegerField(null=False, blank=False, verbose_name="ЄДРПОУ", unique=True)
    title = models.CharField(max_length=150, null=False, blank=False, verbose_name="Назва компанії", unique=True)
    email = models.EmailField(max_length=255, verbose_name="Електронна пошта")
    phone = PhoneNumberField(null=True, blank=False, unique=True, verbose_name="Номер телефону")
    address = models.JSONField(null=True, blank=True, verbose_name="Адреса")
    post_address = models.JSONField(null=True, blank=True, verbose_name="Поштова адреса")

    class Meta:
        db_table = "contractor"
        verbose_name = "Контрагент"
        verbose_name_plural = "Контрагенти"

    def __str__(self):
        return f"{self.title}"
