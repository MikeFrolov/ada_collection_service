from django.db import models

from apps.contractors.models import Contractor
from apps.core.models import Person


class ContractorManager(Person):
    """Manager of the contractor (Manager of the organization providing the case)"""
    class Meta:
        db_table = "сontractor_manager"
        verbose_name = "Менеджер контрагента"
        verbose_name_plural = "Менеджери контрагентів"

    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, verbose_name="Контрагент")
    position = models.CharField(max_length=50, null=False, blank=False, verbose_name="Посада")

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"
