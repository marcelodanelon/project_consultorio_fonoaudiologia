# Generated by Django 4.2.1 on 2023-06-16 01:05

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_localmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='localmodel',
            name='phone1',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Telefone'),
        ),
        migrations.AddField(
            model_name='localmodel',
            name='phone2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Celular'),
        ),
    ]
