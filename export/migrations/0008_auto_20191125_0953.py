# Generated by Django 2.2.7 on 2019-11-25 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('export', '0007_auto_20191125_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imp_libro',
            name='isbn',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]