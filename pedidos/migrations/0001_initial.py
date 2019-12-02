# Generated by Django 2.2.7 on 2019-11-29 11:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bd', '0017_auto_20191125_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('observaciones', models.TextField(blank=True)),
                ('pedido_cliente', models.CharField(max_length=100, unique=True)),
                ('pedido_interno', models.CharField(blank=True, max_length=100)),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True)),
                ('fecha_entrega', models.DateTimeField(auto_now=True)),
                ('copias', models.IntegerField(default=0)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bd.Cliente')),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bd.Libro')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Pedidos',
            },
        ),
    ]