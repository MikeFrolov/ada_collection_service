# Generated by Django 4.1.1 on 2022-11-13 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('debts', '0005_alter_debt_number_from_contractor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='debt',
            name='delay_days',
        ),
    ]
