# Generated by Django 2.2.7 on 2019-11-27 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('export', '0013_auto_20191127_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivo',
            name='cabecera',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]
