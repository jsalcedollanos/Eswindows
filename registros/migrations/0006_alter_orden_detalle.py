# Generated by Django 4.1.5 on 2023-04-29 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0005_orden_detalle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='detalle',
            field=models.CharField(max_length=15, verbose_name='detalle'),
        ),
    ]
