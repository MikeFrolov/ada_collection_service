from django import forms

from .fields import client_form_fields
from .models import Client


class ClientFormFormModel(forms.ModelForm):
    class Meta:
        model = Client
        fields = client_form_fields
