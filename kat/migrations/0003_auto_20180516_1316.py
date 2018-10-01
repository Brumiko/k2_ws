# Generated by Django 2.0.5 on 2018-05-16 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kat', '0002_vrstaclanstva'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrestanakCl',
            fields=[
                ('ozn', models.CharField(max_length=4, primary_key=True, serialize=False, verbose_name='Oznaka')),
                ('naziv', models.TextField(max_length=40, unique=True, verbose_name='Naziv')),
            ],
            options={
                'verbose_name_plural': 'Razlozi prestanka članstva',
                'db_table': 'kat_prestanak_cl',
                'verbose_name': 'Razlog prestanka članstva',
                'ordering': ['naziv'],
            },
        ),
        migrations.RenameModel(
            old_name='ObrStupanj',
            new_name='ObrRazina',
        ),
        migrations.AlterModelOptions(
            name='obrrazina',
            options={'ordering': ['naziv'], 'verbose_name': 'Obrazovna razina', 'verbose_name_plural': 'Obrazovne razine'},
        ),
        migrations.AlterModelTable(
            name='obrrazina',
            table='kat_obr_razina',
        ),
    ]
