# Generated by Django 4.2.1 on 2023-09-25 01:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_alter_localmodel_status'),
        ('atendimento', '0028_alter_contatostelefonicosmodel_ateldata'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudiometriaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auData', models.DateField(default=datetime.date(2023, 9, 24), verbose_name='Data')),
                ('auAudio', models.CharField(blank=True, max_length=50, null=True, verbose_name='Audiômetro')),
                ('auCalib', models.DateField(blank=True, default=datetime.date(2023, 9, 24), null=True, verbose_name='Calibração')),
                ('auMedSo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Médico Solicitante')),
                ('auMVaOe', models.CharField(blank=True, max_length=30, null=True, verbose_name='MASC. VA (OE)')),
                ('auMVoOe', models.CharField(blank=True, max_length=30, null=True, verbose_name='MASC. VO (OE)')),
                ('auMVaOd', models.CharField(blank=True, max_length=30, null=True, verbose_name='MASC. VA (OD)')),
                ('auMVoOd', models.CharField(blank=True, max_length=30, null=True, verbose_name='MASC. VO (OD)')),
                ('auMosPoOe', models.CharField(blank=True, max_length=3, null=True, verbose_name='%')),
                ('auMosdBOe', models.CharField(blank=True, max_length=3, null=True, verbose_name='dB')),
                ('auDisPoOe', models.CharField(blank=True, max_length=3, null=True, verbose_name='%')),
                ('auDisdBOe', models.CharField(blank=True, max_length=3, null=True, verbose_name='dB')),
                ('auSTROe', models.CharField(blank=True, max_length=3, null=True, verbose_name='dB')),
                ('auLDVOe', models.CharField(blank=True, max_length=3, null=True, verbose_name='dB')),
                ('auMascOe', models.CharField(blank=True, max_length=3, null=True, verbose_name='dB')),
                ('auSpaceOe', models.CharField(blank=True, max_length=3, null=True, verbose_name='dB')),
                ('auMosPoOd', models.CharField(blank=True, max_length=3, null=True, verbose_name='%')),
                ('auMosdBOd', models.CharField(blank=True, max_length=3, null=True, verbose_name='dB')),
                ('auDisPoOd', models.CharField(blank=True, max_length=3, null=True, verbose_name='%')),
                ('auDisdBOd', models.CharField(blank=True, max_length=3, null=True, verbose_name='dB')),
                ('auSTROd', models.CharField(blank=True, max_length=3, null=True, verbose_name='dB')),
                ('auLDVOd', models.CharField(blank=True, max_length=3, null=True, verbose_name='dB')),
                ('auMascOd', models.CharField(blank=True, max_length=3, null=True, verbose_name='dB')),
                ('auSpaceOd', models.CharField(blank=True, max_length=3, null=True, verbose_name='dB')),
                ('auObser', models.CharField(blank=True, max_length=60, null=True, verbose_name='Observações')),
                ('aClient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='home.clientmodel', verbose_name='Cliente')),
                ('aLocal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.localmodel', verbose_name='Unidade')),
                ('aProfessional', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.professionalmodel', verbose_name='Profissional')),
            ],
        ),
    ]
