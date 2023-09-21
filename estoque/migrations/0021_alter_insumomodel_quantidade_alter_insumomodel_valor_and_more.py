# Generated by Django 4.2.1 on 2023-09-21 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0020_alter_insumomodel_quantidade_alter_insumomodel_valor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumomodel',
            name='quantidade',
            field=models.CharField(blank=True, default='0', max_length=15, null=True, verbose_name='Quantidade'),
        ),
        migrations.AlterField(
            model_name='insumomodel',
            name='valor',
            field=models.CharField(blank=True, default='0.0', max_length=15, null=True, verbose_name='Valor'),
        ),
        migrations.AlterField(
            model_name='itensinsumomodel',
            name='valorTotal',
            field=models.CharField(max_length=15, null=True, verbose_name='Valor Total'),
        ),
        migrations.AlterField(
            model_name='itensinsumomodel',
            name='valorUnitario',
            field=models.CharField(max_length=15, null=True, verbose_name='Valor Unitario'),
        ),
        migrations.AlterField(
            model_name='itensmovimentacaoinsumomodel',
            name='valorCompra',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Valor Compra'),
        ),
        migrations.AlterField(
            model_name='itensmovimentacaoinsumomodel',
            name='valorTotal',
            field=models.CharField(max_length=15, null=True, verbose_name='Valor Total'),
        ),
        migrations.AlterField(
            model_name='itensmovimentacaoinsumomodel',
            name='valorUnitario',
            field=models.CharField(max_length=15, null=True, verbose_name='Valor Unitario'),
        ),
    ]
