# Generated by Django 4.2.1 on 2023-11-19 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0025_alter_insumomodel_controle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimentacaoinsumomodel',
            name='observacoes',
            field=models.TextField(blank=True, null=True, verbose_name='Observações'),
        ),
    ]
