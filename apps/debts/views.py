from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Debt


class ListDebtsView(ListView):
    template_name = 'debts/list_debts.html'

    def get(self, request, **kwargs):
        filter_parameters = {p: v for p, v in request.GET.items()}

        if not filter_parameters:  # If no filtering parameters are entered
            debts = Debt.objects.all().order_by('id')
        # TODO: Add pagination
        # FIXME: Crashes if using pagination, Conflicting requests '?page=1' and '?age = 1'
            # paginator = Paginator(students, 10)
            # page_number = request.GET.get('page')
            # page_obj = paginator.get_page(page_number)
        # FIXME: Crashes if trying to enter a filter that does not exist
        # TODO: Add filter name check
        else:
            debts = [obj for obj in Debt.objects.filter(**filter_parameters).order_by('id')]
        return render(request, self.template_name, {'debts': debts})  # List debts from database


class CreateDebtFormView(CreateView):  # Fixme: add 'LoginRequiredMixin, ' in first argument
    template_name = 'debts/create_debt_form.html'
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
    success_url = reverse_lazy('list_debts')


class DebtDetailView(DetailView):
    model = Debt
    template_name = 'debts/debt_detail.html'

    def debt_detail_view(self, request, id):
        try:
            debt = Debt.objects.get(pk=id)
        except Debt.DoesNotExist:
            raise Http404('Debt does not exist')

        return render(request, template_name, context={'debt': debt})
