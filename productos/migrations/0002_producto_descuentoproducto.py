# Generated by Django 3.0.4 on 2020-05-19 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descuentoProducto',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]