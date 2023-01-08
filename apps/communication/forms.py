from django import forms

from .fields import create_communication_fields
from .models import Communication
from apps.debts.models import Debt


class CommunicationForm(forms.ModelForm):

    error_css_class = 'error-field'
    required_css_class = 'required-field'
    comment = forms.CharField(widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Коментар/Текст"}))

    class Meta:
        model = Communication
        fields = create_communication_fields
        widgets = {'date_time': forms.HiddenInput()}

    """def __init__(self, *args, **kwargs):
        super(CommunicationForm, self).__init__(self, *args, **kwargs)
        self.fields['comment'].widget.attrs.update({'class': 'form-control'})
        self.fields['debt'] = Debt.objects.get(pk=self.id)"""
