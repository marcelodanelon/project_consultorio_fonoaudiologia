# Generated by Django 4.2.1 on 2023-08-27 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0009_alter_itensinsumomodel_valorunitario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itensinsumomodel',
            name='valorTotal',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Valor Total'),
        ),
    ]