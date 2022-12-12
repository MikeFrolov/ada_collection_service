base_phone_fields = [
                    'phone',
                    'type_phone',
                    'facetime',
                    'signal',
                    'telegram',
                    'viber',
                    'whatsapp',
                    'olx',
                    'prom',
                    'verification'
                    ]
client_phone_fields = [
    'client',
    *base_phone_fields
    ]

client_contact_person_phone_field = [
    'contact_person',
    *base_phone_fields
]

client_email_fields = [
    'client',
    'email',
    'verification'
]

contact_person_email_fields = [
    'contact_person',
    'email',
    'verification'
]