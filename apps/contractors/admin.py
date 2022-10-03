from django.contrib import admin
from .models import Contractor


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "edrpou", "type")
    list_filter = ("id", "title", "edrpou", "type")
    search_fields = ("title__startswith", "edrpou__startswith", )
