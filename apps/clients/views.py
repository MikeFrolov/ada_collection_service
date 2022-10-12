from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Client
from apps.debts.models import Debt


class ListClientsView(ListView):
    template_name = 'clients/list_clients.html'

    def get(self, request, **kwargs):
        filter_parameters = {p: v for p, v in request.GET.items()}

        if not filter_parameters:  # If no filtering parameters are entered
            clients = Client.objects.all().order_by('id')
        else:
            clients = [obj for obj in Client.objects.filter(**filter_parameters).order_by('id')]
        return render(request, self.template_name, {'clients': clients})  # List clients from database


class CreateClientFormView(LoginRequiredMixin, CreateView):
    template_name = 'clients/create_client_form.html'
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
    success_url = reverse_lazy('list_clients')
