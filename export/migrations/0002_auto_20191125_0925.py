# Generated by Django 2.2.7 on 2019-11-25 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('export', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imp_libro',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='imp_libro',
            name='fc',
        ),
        migrations.RemoveField(
            model_name='imp_libro',
            name='fm',
        ),
        migrations.RemoveField(
            model_name='imp_libro',
            name='observaciones',
        ),
        migrations.RemoveField(
            model_name='imp_libro',
            name='uc',
        ),
        migrations.RemoveField(
            model_name='imp_libro',
            name='um',
        ),
    ]
