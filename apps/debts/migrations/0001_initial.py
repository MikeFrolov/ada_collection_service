# Generated by Django 4.1.1 on 2022-09-23 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_sys_number', models.IntegerField(verbose_name='Номер договору в системі')),
                ('contract_origin_number', models.CharField(max_length=20, verbose_name='Оригінальний номер договору')),
                ('currency', models.CharField(blank=True, max_length=50, null=True, verbose_name='Валюта')),
                ('commission', models.IntegerField(verbose_name='Комісія')),
                ('date_of_creation', models.DateField(verbose_name='Дата заключення договору')),
                ('end_date', models.DateField(verbose_name='Дата закінчення договору')),
                ('initial_amount', models.IntegerField(verbose_name='Початкова сума')),
                ('total_amount', models.IntegerField(verbose_name='Загальна сума виданих коштів')),
                ('current_debt', models.IntegerField(verbose_name='Поточний борг')),
                ('amount_of_payments', models.IntegerField(verbose_name='Загальна сума виплат')),
                ('last_payment_date', models.DateTimeField(verbose_name='Дата останнього платежу')),
                ('last_payment_amount', models.IntegerField(verbose_name='Сума останнього платежу')),
                ('total_prolongation_amount', models.IntegerField(blank=True, null=True, verbose_name='Загальна сума пролонгацій')),
                ('loan_body', models.IntegerField(blank=True, null=True, verbose_name='Тіло позики')),
                ('loan_profit', models.IntegerField(blank=True, null=True, verbose_name='Проценти по позиці')),
                ('penalty', models.IntegerField(blank=True, null=True, verbose_name='Пеня')),
                ('fines', models.IntegerField(blank=True, null=True, verbose_name='Штрафи')),
                ('delay_date', models.DateTimeField(verbose_name='Дата виникнення просрочки')),
                ('days_overdue', models.IntegerField(verbose_name='Кількість днів просрочки')),
                ('credit_company', models.CharField(blank=True, max_length=50, null=True, verbose_name='Кредитна компанія')),
                ('credit_brand', models.CharField(blank=True, max_length=50, null=True, verbose_name='Кредитний бренд')),
                ('title_counterparty', models.CharField(blank=True, max_length=50, null=True, verbose_name='Назва контрагента')),
                ('id_counterparty', models.CharField(blank=True, max_length=50, null=True, verbose_name='ID контрагента')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client', verbose_name='Клієнт')),
            ],
        ),
    ]