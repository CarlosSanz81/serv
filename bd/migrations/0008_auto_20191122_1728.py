# Generated by Django 2.2.6 on 2019-11-22 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bd', '0007_modo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modo',
            options={'verbose_name': 'Modo', 'verbose_name_plural': 'Modos'},
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('observaciones', models.TextField(blank=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(blank=True, max_length=200, null=True)),
                ('tel_fijo', models.IntegerField(default=0)),
                ('tel_fijo_ext', models.IntegerField(default=0)),
                ('tel_personal', models.IntegerField(default=0)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bd.Cliente')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
            },
        ),
    ]
