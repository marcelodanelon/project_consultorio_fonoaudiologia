# Generated by Django 4.2.1 on 2023-08-18 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_alter_clientmodel_document1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientmodel',
            name='zipcode',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='CEP'),
        ),
    ]