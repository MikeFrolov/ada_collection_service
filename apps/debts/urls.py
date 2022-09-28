from django.urls import path
from .views import list_clients, list_contractors, list_contractor_managers, list_debts


urlpatterns = [
    path('list_clients/', list_clients),
    path('list_contractors/', list_contractors),
    path('list_contractor_managers/', list_contractor_managers),
    path('list_debts/', list_debts),
]