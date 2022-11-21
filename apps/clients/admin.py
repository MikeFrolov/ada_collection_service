from django.contrib import admin
from .models import Client, ClientContactPerson, ClientStatuses, ClientSocialNetworks
from .fields import client_contact_person_fields


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "last_name", "first_name", "patronymic", "ipn")
    list_per_page = 20
    list_filter = ("last_name", "first_name", "patronymic", "ipn")
    search_fields = ("last_name__startswith", "first_name__startswith", "patronymic__startswith", "ipn__startswith")


@admin.register(ClientStatuses)
class ClientStatusesAdmin(admin.ModelAdmin):
    list_display = ("client", 'military', 'displaced', 'abroad', 'occupation', 'credited', 'bankrupt',
                    'imprisoned', 'illness', 'death'
                    )
    list_per_page = 20
    list_filter = ("client",)


@admin.register(ClientSocialNetworks)
class ClientSocialNetworksAdmin(admin.ModelAdmin):
    list_display = ("client", 'facebook', 'linkedin', 'instagram', 'tictok')
    list_per_page = 20
    list_filter = ("client",)


@admin.register(ClientContactPerson)
class ClientContactPersonAdmin(admin.ModelAdmin):
    fields = client_contact_person_fields
    list_display = ("id", "last_name", "first_name", "patronymic", "client")
    list_per_page = 20
    list_filter = ("last_name", "first_name", "patronymic", "client")
    search_fields = ("last_name__startswith", "first_name__startswith", "patronymic__startswith", "client__startswith")