# Generated by Django 3.0.6 on 2020-05-12 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('facturas', '0001_initial'),
        ('compras', '0001_initial'),
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaPedido', models.DateTimeField(auto_now=True)),
                ('estadoPedido', models.CharField(max_length=30)),
                ('pagoPedido', models.CharField(max_length=30)),
                ('entregaPedido', models.CharField(max_length=30)),
                ('recogerPedido', models.CharField(max_length=30)),
                ('idCompras', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.Compra')),
                ('idEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.Empleado')),
                ('idFactura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturas.Factura')),
            ],
        ),
    ]
