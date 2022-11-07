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
        debt = Debt.objects.get(pk=self.kwargs.get('pk'))

        client_id = debt.client.id  # get client id from pk(request)
        client_addresses = [address for address in ClientAddress.objects.all().filter(person=client_id)]

        context['client_addresses'] = client_addresses
        return context
