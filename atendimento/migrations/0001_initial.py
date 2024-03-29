# Generated by Django 4.2.1 on 2023-06-21 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0028_clientmodel_profissao'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtendimentoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data')),
                ('conheceu', models.CharField(blank=True, max_length=50, null=True)),
                ('question1', models.CharField(blank=True, max_length=50, null=True)),
                ('question2', models.CharField(blank=True, max_length=50, null=True)),
                ('question3', models.CharField(blank=True, max_length=50, null=True)),
                ('question4', models.CharField(blank=True, max_length=50, null=True)),
                ('question5', models.CharField(blank=True, max_length=50, null=True)),
                ('question6a', models.BooleanField(blank=True)),
                ('question6b', models.BooleanField(blank=True)),
                ('question6c', models.BooleanField(blank=True)),
                ('question6d', models.BooleanField(blank=True)),
                ('question6e', models.BooleanField(blank=True)),
                ('question6f', models.BooleanField(blank=True)),
                ('question6g', models.BooleanField(blank=True)),
                ('question6h', models.BooleanField(blank=True)),
                ('question6i', models.BooleanField(blank=True)),
                ('question6j', models.CharField(blank=True, max_length=50, null=True)),
                ('question7a', models.BooleanField(blank=True)),
                ('question7b', models.BooleanField(blank=True)),
                ('question7c', models.BooleanField(blank=True)),
                ('question7d', models.BooleanField(blank=True)),
                ('question7e', models.BooleanField(blank=True)),
                ('question7f', models.BooleanField(blank=True)),
                ('question7g', models.BooleanField(blank=True)),
                ('question7h', models.CharField(blank=True, max_length=50, null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.clientmodel', verbose_name='Cliente')),
            ],
        ),
    ]
