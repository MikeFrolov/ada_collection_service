from django.db import models


messengers = (
            ('facetime', 'FaceTime'),
            ('signal', 'Signal'),
            ('telegram', 'Telegram'),
            ('viber', 'Viber'),
            ('whatsapp', 'WhatsApp'),
)

social_networks = (
                      ('facebook', 'Facebook'),
                      ('linkedin', 'LinkedIn'),
                      ('instagram', 'Instagram'),
)

TYPE_COMMUNICATION_CHOICES = [
    ('IN', 'Вхідний'),
    ('OUT', 'Вихідний'),
]


class TypeCommunicationChoices(models.TextChoices):
    INPUT = 'IN', 'Вхідний',
    OUTPUT = 'OU', 'Вихідний',


INSTRUMENT_CHOICES = [
    ('CALL', 'Дзвінок'),  # A Call
    ('MESS', 'Повідомлення'),  # Message
    ('LETT', 'Лист'),  # Letter
    ('IVM', 'Голосове повідомлення')  # Interactive vice massege
]


COMMUNICATION_CHANNEL_CHOICES = [
    ('Дзвінок', (
        ('phone', 'Телефон'),
        *messengers
    )),
    ('Повідомлення', (
        ('SMS', "СМС"),
        *messengers,
        *social_networks
    )),
    ('Лист', (
        ('email', "Електронний лист"),
        ('mail', "Поштовий лист")
    )),
]

COMMUNICATION_RESULT_CHOICES = [
    ('Результативний дзвінок', (
        ('HU', 'Поклали слухавку'),  # Hung up
        ('DRD', 'Не визнає борг'),  # Does not recognize debt
        ('DNC', 'Клієнта не знають'),  # Don't know the client
        ('BPO', 'Передадуть інформацію'),  # Will be passed on
        ('STD', 'Передано інформацію боржнику'),  # Information was sent to the debtor
    )),
    ('Успішний дзвінок', (
        ('PTP', 'Обіцянка сплатити'),  # Promise to pay
        ('PTE', 'Обіцянка продовження'),  # Promise to extend
        ('RTL', 'Реструтуризація'),  # Restructure
    )),
    ('Не результативний дзвінок', (
        ('ANPH', 'Автовідповідач'),  # Answering machine
        ('DROP', 'Зрив дзвінка'),  # Dropped the call
        ('NINS', 'Номер не обслуговується'),  # Number is not serviced,
        ('INNU', 'Не вірно набранний номер')  # Incorrectly number
    )),
    ('Повідомлення/Лист', (
        ('SEND', 'Відправлено'),  # Send message
        ('RCVD', 'Отримано'),  # Received message
        ('ANSW', 'Отримано відповідь'),  # Answer received
        ('NVLD', 'Не вірні контактні дані'),  # Not valid contact data
    )),
    ('Голосове повідомлення', (
        ('', 'IVM неуспішний'),
        ('', 'IVM повністю прослухано'),
        ('', 'IVM частково прослухано'),
    ))
]
