# Generated by Django 5.0.4 on 2024-05-14 00:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='producto.productocategoria', verbose_name='categoría de producto'),
        ),
    ]