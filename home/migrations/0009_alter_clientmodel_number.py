# Generated by Django 4.2.1 on 2023-05-28 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_clientmodel_born'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientmodel',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Número'),
        ),
    ]
