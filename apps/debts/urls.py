from django.urls import path
from .views import (
    CreateDebtFormView,
    ListDebtsView,
)


urlpatterns = [
    path('create_debt_form/', CreateDebtFormView.as_view(), name='create_debt_form'),
    path('list_debts/', ListDebtsView.as_view(), name='list_debts'),
]