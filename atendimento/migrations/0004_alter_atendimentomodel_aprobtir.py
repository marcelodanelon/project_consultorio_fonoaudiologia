# Generated by Django 4.2.1 on 2023-06-30 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0003_alter_atendimentomodel_aprobtir'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aProbTir',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
