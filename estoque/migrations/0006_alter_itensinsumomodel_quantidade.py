# Generated by Django 4.2.1 on 2023-08-26 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0005_rename_unidade_movimentacaoinsumomodel_local_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itensinsumomodel',
            name='quantidade',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantidade'),
        ),
    ]