# Generated by Django 4.1.1 on 2022-10-04 15:52

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contractors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractorManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Прізвище')),
                ('first_name', models.CharField(max_length=50, verbose_name="Ім'я")),
                ('patronymic', models.CharField(blank=True, max_length=50, null=True, verbose_name='По-батькові')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Дата народження')),
                ('primary_phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, unique=True, verbose_name='Основний номер телефону')),
                ('additional_phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Додатковий номер телефону')),
                ('work_phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Робочий номер телефону')),
                ('home_phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Домашній номер телефону')),
                ('email', models.EmailField(max_length=255, verbose_name='Електронна пошта')),
                ('position', models.CharField(max_length=50, verbose_name='Посада')),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contractors.contractor', verbose_name='Контрагент')),
            ],
            options={
                'verbose_name': 'Менеджер контрагента',
                'verbose_name_plural': 'Менеджери контрагентів',
                'db_table': 'сontractor_manager',
            },
        ),
    ]
