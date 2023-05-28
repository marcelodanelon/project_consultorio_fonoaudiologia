# Generated by Django 4.2.1 on 2023-05-28 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_telefone1_clientmodel_phone1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientmodel',
            name='complement',
            field=models.CharField(blank=True, max_length=15, verbose_name='Complemento'),
        ),
        migrations.AlterField(
            model_name='clientmodel',
            name='born',
            field=models.DateField(verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='clientmodel',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
    ]
