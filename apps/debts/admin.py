from django.contrib import admin
from .models import Client, Contractor, Debt, ContractorManager


@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    list_display = ("id", "contract_origin_number", "client", "currency", "current_debt")
    list_filter = ("contract_origin_number", "client", "currency", "current_debt")
    search_fields = ("contract_origin_number", "current_debt")


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "last_name", "first_name", "patronymic", "ipn")
    list_filter = ("last_name", "first_name", "patronymic", "ipn")
    search_fields = ("last_name__startswith", "first_name__startswith", "patronymic__startswith", "ipn__startswith")


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "edrpou", "type")
    list_filter = ("id", "title", "edrpou", "type")
    search_fields = ("title__startswith", "edrpou__startswith", )


@admin.register(ContractorManager)
class ContractorManagerAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "patronymic", "position", "contractor")
    list_filter = ("last_name", "first_name", "patronymic", "position", "contractor")
    search_fields = (
        "last_name__startswith",
        "first_name__startswith",
        "position__startswith",
        "contractor__startswith", )
