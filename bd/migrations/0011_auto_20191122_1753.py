# Generated by Django 2.2.6 on 2019-11-22 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0010_auto_20191122_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='apellidos',
            field=models.CharField(blank=True, default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contacto',
            name='tel_fijo',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
