# Generated by Django 3.0.4 on 2020-05-17 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_cliente_idusuario'),
        ('valoraciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='valoracion',
            name='idCliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente'),
        ),
    ]