from django.urls import path
from .views import ListContractorsView


urlpatterns = [
    path('list_contractors/', ListContractorsView.as_view(), name='list-contractors'),
]
