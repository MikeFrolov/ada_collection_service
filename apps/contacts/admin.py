from django.contrib import admin
from .models import ClientEmail, ClientPhone, ClientContactPersonEmail, ClientContactPersonPhone
from .fields import client_email_fields, client_phone_fields, contact_person_email_fields, client_contact_person_phone_field


@admin.register(ClientEmail)
class ClientEmailAdmin(admin.ModelAdmin):
    fields = client_email_fields
    list_display = ("client", "email", "verification")
    list_per_page = 25
    list_filter = ("client", "email", "verification")
    search_fields = ("client", "email", "verification")


@admin.register(ClientPhone)
class ClientPhoneAdmin(admin.ModelAdmin):
    fields = client_phone_fields
    list_display = ("client", 'type_phone', "phone", "verification")
    list_per_page = 25
    list_filter = ("client", "phone", "type_phone", "verification")
    search_fields = ("client", "phone", "verification")


@admin.register(ClientContactPersonPhone)
class ClientContactPersonPhoneAdmin(admin.ModelAdmin):
    fields = client_contact_person_phone_field
    list_display = ("contact_person", "type_phone", "phone", "verification")
    list_per_page = 25
    list_filter = ("contact_person", "phone", "type_phone", "verification")
    search_fields = ("contact_person", "phone", "verification")


@admin.register(ClientContactPersonEmail)
class ClientContactPersonEmailAdmin(admin.ModelAdmin):
    fields = contact_person_email_fields
    list_display = ("contact_person", "email", "verification")
    list_per_page = 25
    list_filter = ("contact_person", "email", "verification")
    search_fields = ("contact_person", "email", "verification")
