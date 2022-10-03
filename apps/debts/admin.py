from django.contrib import admin
from .models import Debt


@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    list_display = ("id", "contract_origin_number", "client", "currency", "current_debt")
    list_filter = ("contract_origin_number", "client", "currency", "current_debt")
    search_fields = ("contract_origin_number", "current_debt")
