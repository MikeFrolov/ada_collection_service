from django import forms

from .fields import create_form_fields
from .models import Client


class ClientFormFormModel(forms.ModelForm):
    class Meta:
        model = Client
        fields = create_form_fields
