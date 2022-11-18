from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from datetime import date
from .fields import create_form_fields
from .models import Debt
from apps.adresses.models import ClientAddress
from apps.clients.models import Client, ClientStatuses, ClientSocialNetworks


def get_age(born_date: date) -> int:
    # FIXME: Fix a bug from February 29
    today = date.today()
    return today.year - born_date.year - ((today.month, today.day) < (born_date.month, born_date.day))


def calculate_number_of_days(start_date: date) -> int:
    delta = date.today() - start_date
    return delta.days


class ListDebtsView(ListView):
    template_name = 'debts/list_debts.html'

    def get(self, request, **kwargs):
        filter_parameters = {p: v for p, v in request.GET.items()}

        if not filter_parameters:  # If no filtering parameters are entered
            debts = Debt.objects.all().order_by('id')
        else:
            debts = [obj for obj in Debt.objects.filter(**filter_parameters).order_by('id')]
        return render(request, self.template_name, {'debts': debts})  # List debts from database


class CreateDebtFormView(CreateView):  # Fixme: add 'LoginRequiredMixin, ' in first argument
    template_name = 'debts/create_debt_form.html'
    model = Debt
    fields = create_form_fields
    success_url = reverse_lazy('list_debts')


class DebtDetailView(DetailView):
    model = Debt
    template_name = 'debts/debt_detail_v1.html'

    def get_context_data(self, **kwargs):
        context = super(DebtDetailView, self).get_context_data(**kwargs)
        debt = Debt.objects.get(pk=self.kwargs.get('pk'))  # get client data from db
        client = debt.client  # get client from pk(request)

        context['client_age'] = get_age(debt.client.date_of_birth)  # calculate client age from birthdate

        context['client_addresses'] = [address for address in ClientAddress.objects.all().filter(person=client.id)]  # get client addresses from db

        # Get or create ClientStatuses end added him in context
        try:
            client_statuses = ClientStatuses.objects.get(client=client)
        except ClientStatuses.DoesNotExist:
            client_statuses = ClientStatuses(client=client)
            client_statuses.save()
        context['client_statuses'] = client_statuses  # get client statuses from db

        # Get or create ClientSocialNetworks end added him in context
        try:
            client_networks = ClientSocialNetworks.objects.get(client=debt.client)
        except ClientSocialNetworks.DoesNotExist:
            client_networks = ClientSocialNetworks(client=debt.client)
            client_networks.save()
        context['client_networks'] = client_networks  # get client social networks from db

        context['delay_days'] = calculate_number_of_days(debt.delay_date)

        return context
