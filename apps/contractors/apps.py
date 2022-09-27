from django.apps import AppConfig


class ContractorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.contractor'


class ManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.manager'