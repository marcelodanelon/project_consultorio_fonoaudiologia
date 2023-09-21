# Generated by Django 4.2.1 on 2023-09-21 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0016_alter_grupoinsumomodel_controledecompra'),
    ]

    operations = [
        migrations.AddField(
            model_name='insumomodel',
            name='grupoInsumo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='estoque.grupoinsumomodel', verbose_name='Grupo do Insumo'),
        ),
    ]