from django.contrib import admin
from .models import ClientEmail, ClientPhone, ClientContactPersonPhone
from .fields import create_email_fields, create_phone_fields, client_contact_person_phone_field


@admin.register(ClientEmail)
class ClientEmailAdmin(admin.ModelAdmin):
    fields = create_email_fields
    list_display = ("client", "email")
    list_per_page = 25
    list_filter = ("client", "email")
    search_fields = ("client", "email")


@admin.register(ClientPhone)
class ClientPhoneAdmin(admin.ModelAdmin):
    fields = create_phone_fields
    list_display = ("client", 'type_phone', "phone")
    list_per_page = 25
    list_filter = ("client", "phone", 'type_phone', 'verification')
    search_fields = ("client", "phone", 'verification')


@admin.register(ClientContactPersonPhone)
class ClientContactPersonPhoneAdmin(admin.ModelAdmin):
    fields = client_contact_person_phone_field
    list_display = ("сontact_person", 'type_phone', "phone")
    list_per_page = 25
    list_filter = ("сontact_person", "phone", 'type_phone', 'verification')
    search_fields = ("сontact_person", "phone", 'verification')
