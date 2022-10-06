from django import forms

from .models import Contractor


class ContractorFormFormModel(forms.ModelForm):
    class Meta:
        model = Contractor
        fields = [
            'type',
            'edrpou',
            'title',
            'email',
            'phone',
            'address',
            'post_address'
        ]
