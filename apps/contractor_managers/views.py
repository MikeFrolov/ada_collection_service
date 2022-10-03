from django.http import HttpResponse
from .models import ContractorManager


def list_contractor_managers(request):
    contractor_manager_list = ContractorManager.objects.all()
    output = ' '.join(
        [f'{contractor_manager.last_name} {contractor_manager.first_name} {contractor_manager.patronymic}, '
         f'phone: {contractor_manager.primary_phone_number}, company: {contractor_manager.contractor.title};\n'
         for contractor_manager in contractor_manager_list
         ]
    )
    return HttpResponse(output)
