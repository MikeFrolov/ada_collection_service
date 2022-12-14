from django.db import models


TYPE_CONTRACTOR = [
    ('МФО', 'Мікрофінансова організація'),
    ('ФК', 'Факторингова компанія'),
    ('БУ', 'Банкова установа'),
    ('СК', 'Страхова компанія'),
    ('ТК', 'Телекомунікаційна компанія'),
    ('ЖКГ', 'Житлово-комунальне гопподарство')
]


class VerificationChoices(models.TextChoices):
    Y = "YES", "Валідний"
    N = "NOT", "Не валідний"
