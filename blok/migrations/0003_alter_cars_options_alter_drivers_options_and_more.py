# Generated by Django 4.0.2 on 2022-02-19 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blok', '0002_cars_litsence_drivers_address_drivers_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cars',
            options={'verbose_name': 'Aвтомобили', 'verbose_name_plural': 'Aвтомобили'},
        ),
        migrations.AlterModelOptions(
            name='drivers',
            options={'verbose_name': 'Bодители', 'verbose_name_plural': 'Bодители'},
        ),
        migrations.AlterModelOptions(
            name='litsence',
            options={'verbose_name': 'Лицензии', 'verbose_name_plural': 'Лицензии'},
        ),
        migrations.AlterModelOptions(
            name='putyovka',
            options={'verbose_name': 'Путёвки', 'verbose_name_plural': 'Путёвки'},
        ),
    ]
