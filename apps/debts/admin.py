from django.contrib import admin
from .models import Debt
from .fields import create_form_fields


@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    fields = create_form_fields
    list_display = ("id", "origin_number", "client", "currency", "current_debt")
    list_per_page = 10
    list_filter = ("origin_number", "client", "currency", "current_debt")
    search_fields = ("origin_number", "current_debt")
