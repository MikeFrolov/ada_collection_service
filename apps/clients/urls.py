from django.urls import path
from .views import list_clients


urlpatterns = [
    path('list_clients/', list_clients),
]