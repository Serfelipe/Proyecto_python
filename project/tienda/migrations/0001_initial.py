from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True, verbose_name='descripción')),
            ],
            options={
                'verbose_name': 'categoría de productos',
                'verbose_name_plural': 'categorías de productos',
            },
        ),
    ]