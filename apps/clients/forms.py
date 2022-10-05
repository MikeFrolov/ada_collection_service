from django import forms

from .models import Client


class ClientFormFormModel(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'last_name',
            'first_name',
            'patronymic',
            'date_of_birth',
            'primary_phone_number',
            'additional_phone_number',
            'work_phone_number',
            'home_phone_number',
            'email',
            'ipn',
            'passport_serial',
            'passport_number',
            'addresses',
            'employer',
            'created_date',
            'update_date',
            'comment'
        ]


class ClientForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)