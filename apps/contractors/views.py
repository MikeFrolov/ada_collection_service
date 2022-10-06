from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Contractor


class ListContractorsView(ListView):
    template_name = 'contractors/list_contractors.html'

    def get(self, request, **kwargs):
        filter_parameters = {p: v for p, v in request.GET.items()}

        if not filter_parameters:  # If no filtering parameters are entered
            contractors = Contractor.objects.all().order_by('id')
        # TODO: Add pagination
        # FIXME: Crashes if using pagination, Conflicting requests '?page=1' and '?age = 1'
            # paginator = Paginator(students, 10)
            # page_number = request.GET.get('page')
            # page_obj = paginator.get_page(page_number)
        # FIXME: Crashes if trying to enter a filter that does not exist
        # TODO: Add filter name check
        else:
            contractors = [obj for obj in Contractor.objects.filter(**filter_parameters).order_by('id')]
        return render(request, self.template_name, {'contractors': contractors})  # List contractors from database


class CreateContractorFormView(LoginRequiredMixin, CreateView):
    template_name = 'contractors/create_contractor_form.html'
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
    success_url = reverse_lazy('list_contractors')