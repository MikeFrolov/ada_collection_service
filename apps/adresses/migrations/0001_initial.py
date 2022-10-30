# Generated by Django 4.1.1 on 2022-10-27 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0004_alter_client_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_address', models.CharField(blank=True, choices=[('Legal address', 'Юридична адреса'), ('Physical address', 'Фізична адреса'), ('Work address', 'Робоча адреса'), ('Mailing address', 'Поштова адреса')], default='Legal address', max_length=16, verbose_name='Тип адреси')),
                ('index', models.CharField(blank=True, max_length=8, verbose_name='Індекс')),
                ('country', models.CharField(default='Ukraine', max_length=50, verbose_name='Країна')),
                ('province', models.CharField(max_length=50, verbose_name='Область')),
                ('district', models.CharField(max_length=50, verbose_name='Район')),
                ('type_city', models.CharField(choices=[('с.', 'Село'), ('м.', 'Місто'), ('смт.', 'Селище міського типу')], default='м.', max_length=4, verbose_name='Тип населеного пункту')),
                ('city', models.CharField(max_length=50, verbose_name='Місто')),
                ('city_district', models.CharField(blank=True, max_length=50, verbose_name='Район-міста')),
                ('type_street', models.CharField(choices=[('просп.', 'Проспект'), ('вул.', 'Вулиця'), ('пров.', 'Провулок')], default='вул.', max_length=6, verbose_name='Тип вулиці')),
                ('street', models.CharField(max_length=50, verbose_name='Вулиця')),
                ('house', models.CharField(max_length=9, verbose_name='Будинок')),
                ('apartment_type', models.CharField(blank=True, choices=[('кв.', 'Квартира'), ('оф.', 'Офіс')], max_length=9, verbose_name='Тип приміщення')),
                ('apartment_number', models.IntegerField(blank=True, verbose_name='Номер приміщення')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client', verbose_name='Клієнт')),
            ],
            options={
                'verbose_name': 'Адреса клієнта',
                'verbose_name_plural': 'Адреси клієнтів',
                'db_table': 'client_address',
            },
        ),
    ]
