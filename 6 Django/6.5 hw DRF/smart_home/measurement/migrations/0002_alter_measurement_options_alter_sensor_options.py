# Generated by Django 4.2.4 on 2023-09-18 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measurement',
            options={'ordering': ['data_measure'], 'verbose_name': 'Измерение', 'verbose_name_plural': 'Измерения'},
        ),
        migrations.AlterModelOptions(
            name='sensor',
            options={'ordering': ['id'], 'verbose_name': 'Датчик', 'verbose_name_plural': 'Датчики'},
        ),
    ]