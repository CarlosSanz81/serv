# Generated by Django 2.2.7 on 2019-11-22 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bd', '0005_auto_20191122_0845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formato_Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('observaciones', models.TextField(blank=True)),
                ('formatotxt', models.CharField(max_length=50)),
                ('ancho', models.FloatField(default=0)),
                ('largo', models.FloatField(default=0)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Formato Libro',
                'verbose_name_plural': 'Formatos Libro',
            },
        ),
    ]
