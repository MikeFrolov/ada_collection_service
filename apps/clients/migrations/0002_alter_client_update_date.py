# Generated by Django 4.1.1 on 2022-09-27 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='update_date',
            field=models.DateTimeField(verbose_name='Дата оновлення'),
        ),
    ]
