from django.contrib import admin
from .models import ContractorManager


@admin.register(ContractorManager)
class ContractorManagerAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "patronymic", "position", "contractor")
    list_per_page = 10
    list_filter = ("last_name", "first_name", "patronymic", "position", "contractor")
    search_fields = (
        "last_name__startswith",
        "first_name__startswith",
        "position__startswith",
        "contractor__startswith", )
