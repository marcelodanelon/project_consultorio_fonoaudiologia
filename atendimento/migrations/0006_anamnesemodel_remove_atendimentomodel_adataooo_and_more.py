# Generated by Django 4.2.1 on 2023-07-02 12:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0005_alter_atendimentomodel_ajatesap_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnamneseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aIDAtend', models.IntegerField()),
                ('aDataAna', models.DateField(default=datetime.date(2023, 7, 2))),
                ('aAjustOD', models.CharField(blank=True, max_length=50, null=True)),
                ('aAjustOE', models.CharField(blank=True, max_length=50, null=True)),
                ('aObserva', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='atendimentomodel',
            name='aDataOOO',
        ),
        migrations.AddField(
            model_name='atendimentomodel',
            name='aClikOOD',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='atendimentomodel',
            name='aClikOOE',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='atendimentomodel',
            name='aComClik',
            field=models.CharField(blank=True, choices=[('sim', 'Sim'), ('não', 'Não')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='atendimentomodel',
            name='aDataPri',
            field=models.DateField(null=True, verbose_name='Data 1ª consulta'),
        ),
        migrations.AddField(
            model_name='atendimentomodel',
            name='aInfoTec',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='atendimentomodel',
            name='aReceOOD',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='atendimentomodel',
            name='aReceOOE',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='atendimentomodel',
            name='aSemClik',
            field=models.CharField(blank=True, choices=[('sim', 'Sim'), ('não', 'Não')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='atendimentomodel',
            name='aTuboOOD',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='atendimentomodel',
            name='aTuboOOE',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
