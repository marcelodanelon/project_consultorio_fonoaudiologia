# Generated by Django 4.2.1 on 2023-07-02 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0010_alter_anamnesemodel_aidatend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anamnesemodel',
            name='aIDAtend',
            field=models.IntegerField(),
        ),
    ]
