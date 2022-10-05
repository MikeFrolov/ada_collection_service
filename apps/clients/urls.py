from django.urls import path
from .views import (
    CreateClientFormView,
    ListClientsView,
)

urlpatterns = [
    path('create_client_form/', CreateClientFormView.as_view(), name='create_client_form'),
    path('list_clients/', ListClientsView.as_view(), name='list_clients'),
]
