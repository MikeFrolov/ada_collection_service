from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.base import View
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Communication
from .fields import create_communication_fields


class ListCommunicationView(ListView):
    template_name = 'communication/list_communication.html'

    def get(self, request, **kwargs):
        filter_parameters = {p: v for p, v in request.GET.items()}
        if not filter_parameters:  # If no filtering parameters are entered
            communication_history = Communication.objects.all().order_by('-date_time')
        else:
            communication_history = [obj for obj in Communication.objects.filter(**filter_parameters).order_by('date_time')]
        return render(request, self.template_name, {'communication_history': communication_history})  # List communication from database


class CreateCommunication(CreateView):  # TODO: add 'LoginRequiredMixin, ' in first argument
    def get_queryset(self):
        # original qs
        qs = super().get_queryset()
        # filter by a variable captured from url, for example
        return qs.filter(name__startswith=self.kwargs['debt'])

    template_name = 'communication/create_communication_form.html'
    model = Communication
    fields = create_communication_fields
    success_url = reverse_lazy('list_communications')
