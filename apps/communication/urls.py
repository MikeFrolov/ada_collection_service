from django.urls import path
from .views import (
    CreateCommunication,
    ListCommunicationView,
)

urlpatterns = [
    path('create_communication/', CreateCommunication.as_view(), name='create_communication'),
    path('list_communications/', ListCommunicationView.as_view(), name='list_communications'),
]
