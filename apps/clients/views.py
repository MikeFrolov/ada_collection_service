from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Client
from apps.debts.models import Debt


# todo: Написати функцію що повертає список справ фільтрованих по клієнту, передати цей список в шаблон "List_clients"
def list_client_debts(clients_list):
    clients_debts = {}
    for client in clients_list:
        clients_debts[client.id] = [debt for debt in Debt.objects.filter(client.id)]
    return clients_debts


class ListClientsView(ListView):
    template_name = 'clients/list_clients.html'

    def get(self, request, **kwargs):
        filter_parameters = {p: v for p, v in request.GET.items()}

        if not filter_parameters:  # If no filtering parameters are entered
            clients = Client.objects.all().order_by('id')
        # TODO: Add pagination
        # FIXME: Crashes if using pagination, Conflicting requests '?page=1' and '?age = 1'
            # paginator = Paginator(students, 10)
            # page_number = request.GET.get('page')
            # page_obj = paginator.get_page(page_number)
        # FIXME: Crashes if trying to enter a filter that does not exist
        # TODO: Add filter name check
        else:
            clients = [obj for obj in Client.objects.filter(**filter_parameters).order_by('id')]
            client_debts = list_client_debts(clients)
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