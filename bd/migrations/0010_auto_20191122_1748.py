# Generated by Django 2.2.6 on 2019-11-22 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0009_auto_20191122_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='tel_fijo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='tel_fijo_ext',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='tel_personal',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
