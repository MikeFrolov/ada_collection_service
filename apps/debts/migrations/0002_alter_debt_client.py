# Generated by Django 4.1.1 on 2022-09-27 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('debts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='debts.client', verbose_name='Клієнт'),
        ),
    ]
