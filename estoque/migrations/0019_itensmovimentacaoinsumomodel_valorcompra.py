# Generated by Django 4.2.1 on 2023-09-21 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0018_insumomodel_controle_alter_insumomodel_situacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='itensmovimentacaoinsumomodel',
            name='valorCompra',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Valor Unitario'),
        ),
    ]