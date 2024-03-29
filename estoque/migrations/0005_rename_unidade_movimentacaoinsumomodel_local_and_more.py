# Generated by Django 4.2.1 on 2023-08-26 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_alter_clientmodel_phone1_alter_clientmodel_phone2_and_more'),
        ('estoque', '0004_itensinsumomodel_movimentacao_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movimentacaoinsumomodel',
            old_name='unidade',
            new_name='local',
        ),
        migrations.AlterField(
            model_name='itensinsumomodel',
            name='local',
            field=models.ForeignKey(default='UNIDADE', null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.localmodel', verbose_name='Unidade'),
        ),
        migrations.AlterField(
            model_name='itensinsumomodel',
            name='valorTotal',
            field=models.FloatField(blank=True, null=True, verbose_name='Valor Total'),
        ),
        migrations.AlterField(
            model_name='itensinsumomodel',
            name='valorUnitario',
            field=models.FloatField(blank=True, null=True, verbose_name='Valor Unitario'),
        ),
    ]
