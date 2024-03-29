# Generated by Django 4.2.1 on 2023-08-17 22:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_clientmodel_profissao'),
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itensinsumomodel',
            name='marca',
        ),
        migrations.RemoveField(
            model_name='itensinsumomodel',
            name='vencimento',
        ),
        migrations.AddField(
            model_name='insumomodel',
            name='marca',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='estoque.marcamodel', verbose_name='Marca'),
        ),
        migrations.AddField(
            model_name='insumomodel',
            name='situacao',
            field=models.BooleanField(default=True, verbose_name='Situação'),
        ),
        migrations.AddField(
            model_name='itensinsumomodel',
            name='dataEntrada',
            field=models.DateField(default=datetime.date.today, verbose_name='Data de Entrada'),
        ),
        migrations.AddField(
            model_name='itensinsumomodel',
            name='dataValidade',
            field=models.DateField(default=datetime.date.today, verbose_name='Data de Validade'),
        ),
        migrations.AddField(
            model_name='itensinsumomodel',
            name='local',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.localmodel', verbose_name='Unidade'),
        ),
        migrations.AddField(
            model_name='itensinsumomodel',
            name='serie',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Serie'),
        ),
    ]
