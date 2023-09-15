# Generated by Django 4.2.1 on 2023-09-15 17:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0024_alter_anamnesemodel_adataana_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anamnesemodel',
            name='aDataAna',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aDataPri',
            field=models.DateField(null=True, verbose_name='Data 1ª consulta'),
        ),
    ]
