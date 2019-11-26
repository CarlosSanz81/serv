# Generated by Django 2.2.7 on 2019-11-25 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('export', '0009_auto_20191125_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imp_libro',
            name='dato_variable',
            field=models.CharField(default='no', max_length=10),
        ),
        migrations.AlterField(
            model_name='imp_libro',
            name='formato_libro',
            field=models.CharField(default='no hay formato', max_length=20),
        ),
        migrations.AlterField(
            model_name='imp_libro',
            name='gramaje',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='imp_libro',
            name='no_paginas',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='imp_libro',
            name='papel',
            field=models.CharField(default='no hay papel', max_length=200),
        ),
        migrations.AlterField(
            model_name='imp_libro',
            name='solapas',
            field=models.CharField(default='NO', max_length=10),
        ),
    ]