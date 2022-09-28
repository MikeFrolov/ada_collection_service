from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Contractor, ContractorManager, Debt


def list_clients(request):
    clients_list = Client.objects.all()
    output = ' '.join(
        [f'{client.first_name} {client.last_name} {client.patronymic},'
         f'{client.primary_phone_number};\n'
         for client in clients_list
         ]
    )
    return HttpResponse(output)


def list_contractors(request):
    contractor_list = Contractor.objects.all()
    output = ' '.join(
        [f'{contractor.type}, {contractor.title}, {contractor.edrpou}, {contractor.email};'
         for contractor in contractor_list
         ]
    )
    return HttpResponse(output)


def list_contractor_managers(request):
    contractor_manager_list = ContractorManager.objects.all()
    output = ' '.join(
        [f'{contractor_manager.last_name} {contractor_manager.first_name} {contractor_manager.patronymic}, '
         f'phone: {contractor_manager.primary_phone_number}, company: {contractor_manager.contractor.title};\n'
         for contractor_manager in contractor_manager_list
         ]
    )
    return HttpResponse(output)


def list_debts(request):
    debts_list = Debt.objects.all()
    output = ' '.join(
        [f'ID: {debt.id}, {debt.contract_origin_number}, client: {debt.client},'
         f'currency: {debt.currency}, contractor: {debt.title_contractor};\n' for debt in debts_list]
    )
    return HttpResponse(output)
