# Generated by Django 4.2.1 on 2023-09-13 23:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_clientmodel_age_alter_clientmodel_status'),
        ('estoque', '0012_alter_itensinsumomodel_movimentacao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItensMovimentacaoInsumoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valorUnitario', models.CharField(max_length=10, null=True, verbose_name='Valor Unitario')),
                ('valorTotal', models.CharField(max_length=10, null=True, verbose_name='Valor Total')),
                ('quantidade', models.IntegerField(null=True, verbose_name='Quantidade')),
                ('dataValidade', models.DateField(default=datetime.date.today, verbose_name='Data de Validade')),
                ('dataEntrada', models.DateField(default=datetime.date.today, verbose_name='Data de Entrada')),
                ('serie', models.CharField(max_length=20, null=True, verbose_name='Serie/Lote')),
                ('insumo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='estoque.insumomodel', verbose_name='Insumo')),
                ('local', models.ForeignKey(default='UNIDADE', null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.localmodel', verbose_name='Unidade')),
                ('movimentacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='estoque.movimentacaoinsumomodel')),
            ],
        ),
    ]
