# Generated by Django 2.2.7 on 2019-11-24 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0014_auto_20191124_1011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='libro',
            options={'verbose_name': 'Libro', 'verbose_name_plural': 'Libros'},
        ),
        migrations.RemoveField(
            model_name='libro',
            name='preimpresion',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='ultima_impresion',
        ),
    ]
