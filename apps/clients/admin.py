from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "last_name", "first_name", "patronymic", "ipn")
    list_per_page = 10
    list_filter = ("last_name", "first_name", "patronymic", "ipn")
    search_fields = ("last_name__startswith", "first_name__startswith", "patronymic__startswith", "ipn__startswith")
