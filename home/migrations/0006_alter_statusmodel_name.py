# Generated by Django 4.2.1 on 2023-05-28 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_statemodel_clientmodel_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusmodel',
            name='name',
            field=models.CharField(default='Ativo', max_length=40),
        ),
    ]
