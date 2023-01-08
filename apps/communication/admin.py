from django.contrib import admin
from .models import Communication


@admin.register(Communication)
class CommunicationAdmin(admin.ModelAdmin):
    fields = ['debt', 'date_time', 'type', 'action', 'communication_channel', 'communication_detail', 'person', 'result', 'sum', 'pay_date', 'comment']
    list_display = ('debt', 'date_time', 'type', 'action', 'communication_channel', 'person')
    list_per_page = 20
    list_filter = ('debt', 'date_time', 'type', 'action', 'communication_channel', 'person')
    search_fields = ()
