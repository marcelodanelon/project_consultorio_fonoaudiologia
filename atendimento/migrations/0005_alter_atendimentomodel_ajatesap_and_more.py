# Generated by Django 4.2.1 on 2023-06-30 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0004_alter_atendimentomodel_aprobtir'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aJaTesAp',
            field=models.CharField(blank=True, choices=[('sim', 'Sim'), ('não', 'Não')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aJaUsoAp',
            field=models.CharField(blank=True, choices=[('sim', 'Sim'), ('não', 'Não')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='atendimentomodel',
            name='aSituaca',
            field=models.CharField(blank=True, choices=[('Em Andamento', 'Em Andamento'), ('Concluído', 'Concluído')], max_length=15, null=True),
        ),
    ]