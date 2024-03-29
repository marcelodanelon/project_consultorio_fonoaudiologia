# Generated by Django 4.2.1 on 2023-10-05 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0037_alter_localmodel_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agDatIni', models.DateField(verbose_name='Data Início')),
                ('agDatFim', models.DateField(verbose_name='Data Final')),
                ('agHorIni', models.TimeField(verbose_name='Horário Início')),
                ('agHorFim', models.TimeField(verbose_name='Horário Final')),
                ('agTipAge', models.CharField(choices=[['quantidade', 'Quantidade'], ['quantidadeTempo', 'Quantidade por tempo']], default='quantidade', max_length=30, verbose_name='Tipo de Agenda')),
                ('agQtdTot', models.IntegerField(verbose_name='Quantidade')),
                ('agQtdTem', models.IntegerField(verbose_name='Tempo')),
                ('aLocal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.localmodel', verbose_name='Unidade')),
                ('aProfessional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.professionalmodel', verbose_name='Profissional')),
            ],
        ),
        migrations.CreateModel(
            name='AgendamentoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agDataAg', models.DateField(verbose_name='Data Agendamento')),
                ('agHoraAg', models.TimeField(verbose_name='Horário Agendamento')),
                ('agObserv', models.CharField(blank=True, max_length=100, null=True, verbose_name='Observações')),
                ('aClient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.clientmodel', verbose_name='Cliente')),
                ('aLocal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.localmodel', verbose_name='Unidade')),
                ('aProfessional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.professionalmodel', verbose_name='Profissional')),
            ],
        ),
    ]
