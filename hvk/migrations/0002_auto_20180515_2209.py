# Generated by Django 2.0.5 on 2018-05-15 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hvk', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clan',
            name='py_user',
        ),
        migrations.DeleteModel(
            name='Clan',
        ),
    ]
