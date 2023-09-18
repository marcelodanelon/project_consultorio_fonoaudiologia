# Generated by Django 4.2.1 on 2023-09-15 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_alter_professionalmodel_responsiblename_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientmodel',
            old_name='profissao',
            new_name='profession',
        ),
        migrations.AddField(
            model_name='clientmodel',
            name='typeRegister',
            field=models.CharField(choices=[('simplificado', 'Simplificado'), ('completo', 'Completo')], default=1, max_length=15),
        ),
    ]