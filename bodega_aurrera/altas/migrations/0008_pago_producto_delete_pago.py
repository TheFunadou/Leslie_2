# Generated by Django 4.2.4 on 2023-12-06 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('altas', '0007_pago_delete_pago_articulos'),
    ]

    operations = [
        migrations.CreateModel(
            name='pago_producto',
            fields=[
                ('serial', models.BigAutoField(primary_key=True, serialize=False)),
                ('folio', models.BigIntegerField()),
                ('cantidad', models.IntegerField()),
                ('precio', models.FloatField()),
                ('fecha_hora', models.DateTimeField(auto_now_add=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='altas.alta_de_productos')),
            ],
            options={
                'unique_together': {('serial', 'folio', 'producto')},
            },
        ),
        migrations.DeleteModel(
            name='pago',
        ),
    ]
