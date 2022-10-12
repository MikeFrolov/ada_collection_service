from django.urls import path
from .views import (
    CreateContractorFormView,
    ListContractorsView,
)


urlpatterns = [
    path('create_contractor_form/', CreateContractorFormView.as_view(), name='create_contractor_form'),
    path('list_contractors/', ListContractorsView.as_view(), name='list_contractors'),
]
