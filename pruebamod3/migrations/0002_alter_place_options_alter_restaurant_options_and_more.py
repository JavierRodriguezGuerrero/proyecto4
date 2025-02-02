# Generated by Django 5.1.4 on 2025-01-24 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pruebamod3', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['id'], 'verbose_name': 'Place'},
        ),
        migrations.AlterModelOptions(
            name='restaurant',
            options={'ordering': ['place'], 'verbose_name': 'Restaurant'},
        ),
        migrations.AlterModelOptions(
            name='waiter',
            options={'ordering': ['id'], 'verbose_name': 'Waiter'},
        ),
        migrations.AlterModelTable(
            name='place',
            table='Place',
        ),
        migrations.AlterModelTable(
            name='restaurant',
            table='Restaurant',
        ),
        migrations.AlterModelTable(
            name='waiter',
            table='Waiter',
        ),
    ]
