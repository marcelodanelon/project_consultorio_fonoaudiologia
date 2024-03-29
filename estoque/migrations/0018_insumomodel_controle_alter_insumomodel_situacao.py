# Generated by Django 4.2.1 on 2023-09-21 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0017_insumomodel_grupoinsumo'),
    ]

    operations = [
        migrations.AddField(
            model_name='insumomodel',
            name='controle',
            field=models.CharField(choices=[('lote', 'Lote'), ('quantidade', 'Quantidade')], default=1, max_length=10, verbose_name='Tipo de Controle'),
        ),
        migrations.AlterField(
            model_name='insumomodel',
            name='situacao',
            field=models.CharField(choices=[('sim', 'Sim'), ('nao', 'Não')], default=1, max_length=3, verbose_name='Situação'),
        ),
    ]
