from django.contrib import admin

from .models import Contractor, Manager


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "edrpou", "type")
    list_filter = ("id", "title", "edrpou", "type")
    search_fields = ("title__startswith", "edrpou__startswith", )


@admin.register(Manager)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "patronymic", "position", "contractor")
    list_filter = ("last_name", "first_name", "patronymic", "position", "contractor")
    search_fields = (
        "last_name__startswith",
        "first_name__startswith",
        "position__startswith",
        "contractor__startswith", )