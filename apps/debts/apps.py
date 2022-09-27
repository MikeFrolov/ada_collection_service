from django.apps import AppConfig


class ClientConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.clients'


class ContractorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.contractor'


class ManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.manager'


class DebtsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.debt'
