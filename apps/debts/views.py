from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
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
