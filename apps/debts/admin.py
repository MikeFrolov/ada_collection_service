from django.contrib import admin
from .models import Debt


@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    list_display = ("id", "origin_number", "client", "currency", "current_debt")
    list_filter = ("origin_number", "client", "currency", "current_debt")
    search_fields = ("origin_number", "current_debt")
