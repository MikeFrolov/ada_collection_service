from django.http import HttpResponse

from .models import Client


def list_clients(request):
    clients_list = Client.objects.all()
    output = ' '.join(
        [f'{client.first_name} {client.last_name} {client.patronymic},'
         f'{client.primary_phone_number};\n'
         for client in clients_list
         ]
    )
    return HttpResponse(output)
