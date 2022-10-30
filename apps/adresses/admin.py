from django.contrib import admin
from .fields import fields
from .models import ClientAddress, ContractorAddress, ContractorManagerAddress


list_display = ("id", "person", "index", "country", "city")
list_per_page = 20
list_filter = ("id", "person", "country", "city")
search_fields = ("id", "person", "country", "city")


@admin.register(ClientAddress)
class ClientAddressAdmin(admin.ModelAdmin):
    fields = fields  # Order of fields in the form (admin)
    list_display = list_display
    list_per_page = list_per_page
    list_filter = list_filter
    search_fields = search_fields


@admin.register(ContractorAddress)
class ContractorAddressAdmin(admin.ModelAdmin):
    fields = fields  # Order of fields in the form (admin)
    list_display = list_display
    list_per_page = list_per_page
    list_filter = list_filter
    search_fields = search_fields


@admin.register(ContractorManagerAddress)
class ContractorManagerAddressAdmin(admin.ModelAdmin):
    fields = fields  # Order of fields in the form (admin)
    list_display = list_display
    list_per_page = list_per_page
    list_filter = list_filter
    search_fields = search_fields
