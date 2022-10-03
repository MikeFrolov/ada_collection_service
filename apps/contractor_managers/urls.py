from django.urls import path
from .views import list_contractor_managers


urlpatterns = [
    path('list_contractor_managers/', list_contractor_managers),
]