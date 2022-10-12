from django import forms

from .models import Debt


class ClientFormFormModel(forms.ModelForm):
    class Meta:
        model = Debt
        fields = [
            'origin_number',
            'number_from_contractor',
            'client',
            'date_of_creation',
            'end_date',
            'credit_company',
            'credit_brand',
            'title_contractor',
            'payment_amounts',
            'number_of_late_payments',
            'monthly_payment_amount',
            'initial_amount',
            'total_issued_amount',
            'amount_of_payments',
            'principal',
            'commission',
            'interest',
            'penalty',
            'fines',
            'current_debt',
            'total_prolongation_amount',
            'last_payment_date',
            'last_payment_amount',
            'currency',
            'delay_date',
            'delay_days',
        ]
