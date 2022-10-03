from django.urls import path
from .views import ListDebtsView


urlpatterns = [
    path('list_debts/', ListDebtsView.as_view(), name='list-debts'),
]