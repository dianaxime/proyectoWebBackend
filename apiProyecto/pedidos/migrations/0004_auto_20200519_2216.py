# Generated by Django 3.0.4 on 2020-05-20 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_remove_pedido_idcompras'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='fechaPedido',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
