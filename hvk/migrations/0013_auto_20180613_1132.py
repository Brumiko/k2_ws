# Generated by Django 2.0.5 on 2018-06-13 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hvk', '0012_auto_20180612_1621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kontaktcl',
            old_name='po',
            new_name='clan',
        ),
    ]
