# Generated by Django 2.2.7 on 2019-11-26 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('export', '0010_auto_20191125_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]