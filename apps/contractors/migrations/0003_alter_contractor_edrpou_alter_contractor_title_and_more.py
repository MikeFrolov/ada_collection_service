# Generated by Django 4.1.1 on 2022-10-06 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractors', '0002_alter_contractor_title_alter_contractor_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='edrpou',
            field=models.IntegerField(unique=True, verbose_name='ЄДРПОУ'),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='title',
            field=models.CharField(max_length=150, unique=True, verbose_name='Назва компанії'),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='type',
            field=models.CharField(choices=[('МФО', 'Мікрофінансова організація'), ('ФК', 'Факторингова компанія'), ('БАНК', 'Банкова установа'), ('СК', 'Страхова компанія'), ('ТК', 'Телекомунікаційна компанія'), ('ЖКГ', 'Житлово-комунальне гопподарство'), ('ФГВ', 'Фонд гарантування вкладів')], default='МФО', max_length=4, verbose_name='Тип контрагента'),
        ),
    ]