# Generated by Django 4.2.1 on 2023-09-20 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0026_contatostelefonicosmodel_atendimentomodel_ademanda_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contatostelefonicosmodel',
            name='aIDAtend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='atendimento.atendimentomodel'),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aDemanda',
            field=models.CharField(choices=[('espontanea', 'Espontânea'), ('telefone', 'Telefone'), ('agendamento', 'Agendamento')], default='espontanea', max_length=15, verbose_name='Demanda'),
        ),
        migrations.AlterField(
            model_name='contatostelefonicosmodel',
            name='aDemanda',
            field=models.CharField(choices=[('telefone', 'Telefone'), ('espontanea', 'Espontânea'), ('agendamento', 'Agendamento')], default=2, max_length=15, verbose_name='Demanda'),
        ),
        migrations.AlterField(
            model_name='contatostelefonicosmodel',
            name='aTelObse',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Observações'),
        ),
    ]