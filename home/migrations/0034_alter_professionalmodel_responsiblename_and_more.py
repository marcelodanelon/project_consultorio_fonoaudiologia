# Generated by Django 4.2.1 on 2023-09-15 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_clientmodel_age_alter_clientmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionalmodel',
            name='responsibleName',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Pessoa para Recados'),
        ),
        migrations.AlterField(
            model_name='professionalmodel',
            name='status',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.statusmodel', verbose_name='Situação'),
        ),
    ]
