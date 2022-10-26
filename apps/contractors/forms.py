from django import forms

from .fields import create_form_fields
from .models import Contractor


class ContractorFormFormModel(forms.ModelForm):
    class Meta:
        model = Contractor
        fields = create_form_fields
