# Generated by Django 3.0.4 on 2020-05-20 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_auto_20200519_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='descuentoCompra',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
