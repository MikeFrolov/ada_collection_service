# Generated by Django 4.1.1 on 2022-10-05 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debts', '0002_alter_debt_amount_of_payments_alter_debt_commission_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt',
            name='date_of_creation',
            field=models.DateField(help_text='format: 01.01.2000', verbose_name='Дата заключення договору'),
        ),
    ]