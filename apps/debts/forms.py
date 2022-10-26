from django import forms

from .fields import create_form_fields
from .models import Debt


class ClientFormFormModel(forms.ModelForm):
    class Meta:
        model = Debt
        fields = create_form_fields
