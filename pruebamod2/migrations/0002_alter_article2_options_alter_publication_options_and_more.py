# Generated by Django 5.1.4 on 2025-01-24 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pruebamod2', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article2',
            options={'ordering': ['headline'], 'verbose_name': 'Article2'},
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ['title'], 'verbose_name': 'Publication'},
        ),
        migrations.AlterModelTable(
            name='article2',
            table='Article2',
        ),
        migrations.AlterModelTable(
            name='publication',
            table='Publication',
        ),
    ]
