# Generated by Django 4.0.2 on 2022-02-20 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blok', '0010_alter_drivers_options_alter_drivers_passport_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cars',
            options={'ordering': ('number',), 'verbose_name': 'Aвтомобили', 'verbose_name_plural': 'Aвтомобили'},
        ),
        migrations.AlterModelOptions(
            name='litsence',
            options={'ordering': ('number',), 'verbose_name': 'Лицензии', 'verbose_name_plural': 'Лицензии'},
        ),
        migrations.AlterModelOptions(
            name='putyovka',
            options={'ordering': ('date',), 'verbose_name': 'Путёвки', 'verbose_name_plural': 'Путёвки'},
        ),
    ]
