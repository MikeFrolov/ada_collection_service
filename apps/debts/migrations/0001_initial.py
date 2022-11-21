# Generated by Django 4.1.3 on 2022-11-21 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contractors', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debt_type', models.CharField(choices=[('Короткостроковий', 'Короткостроковий'), ('Довгостроковий', 'Довгостроковий'), ('Овердрафт', 'Овердрафт'), ('Споживчий', 'Споживчий'), ('Кредитна лінія', 'Кредитна лінія'), ('Забезпечений заставою', 'Забезпечений заставою')], default='Короткостроковий', max_length=21, verbose_name='Тип договору')),
                ('origin_number', models.CharField(max_length=15, verbose_name='Оригінальний номер договору')),
                ('number_from_contractor', models.CharField(max_length=15, verbose_name='Номер договору в системі контрагента')),
                ('date_of_creation', models.DateField(help_text='format: 01.01.2000', verbose_name='Дата заключення договору')),
                ('end_date', models.DateField(verbose_name='Дата закінчення договору')),
                ('credit_company', models.CharField(blank=True, max_length=50, null=True, verbose_name='Кредитна компанія')),
                ('credit_brand', models.CharField(blank=True, max_length=50, null=True, verbose_name='Кредитний бренд')),
                ('payment_amounts', models.IntegerField(default=0, verbose_name='Кількість платежів')),
                ('number_of_late_payments', models.IntegerField(default=0, verbose_name='Кількість прострочених платежів')),
                ('monthly_payment_amount', models.FloatField(default=0, verbose_name='Сума щомісячного платежу')),
                ('initial_amount', models.FloatField(default=0, verbose_name='Початкова сума')),
                ('total_issued_amount', models.FloatField(default=0, verbose_name='Загальна сума виданих коштів')),
                ('amount_of_payments', models.IntegerField(default=0, verbose_name='Загальна сума виплат')),
                ('principal', models.FloatField(blank=True, default=0, null=True, verbose_name='Основний борг')),
                ('commission', models.FloatField(default=0, verbose_name='Комісії')),
                ('interest', models.FloatField(blank=True, default=0, null=True, verbose_name='Відсотки')),
                ('penalty', models.FloatField(blank=True, default=0, null=True, verbose_name='Пеня')),
                ('fines', models.FloatField(blank=True, default=0, null=True, verbose_name='Штрафи')),
                ('current_debt', models.FloatField(default=0, verbose_name='Поточний борг')),
                ('total_prolongation_amount', models.FloatField(blank=True, default=0, null=True, verbose_name='Загальна сума пролонгацій')),
                ('last_payment_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата останнього платежу')),
                ('last_payment_amount', models.FloatField(blank=True, default=0, max_length=8, null=True, verbose_name='Сума останнього платежу')),
                ('currency', models.CharField(choices=[('USD', 'US Dollar'), ('EUR', 'Euro'), ('UAH', 'Гривня')], default='UAH', max_length=3, verbose_name='Валюта')),
                ('delay_date', models.DateField(verbose_name='Дата виникнення просрочки')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='clients.client', verbose_name='Клієнт')),
                ('title_contractor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='contractors.contractor', verbose_name='Назва контрагента')),
            ],
            options={
                'verbose_name': 'Справа',
                'verbose_name_plural': 'Справи',
                'db_table': 'debt',
            },
        ),
    ]
