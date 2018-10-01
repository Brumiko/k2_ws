# Generated by Django 2.0.5 on 2018-05-21 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kat', '0006_auto_20180517_1009'),
        ('hvk', '0010_auto_20180521_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clanstvo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dat_od', models.DateField(verbose_name='Od')),
                ('dat_do', models.DateField(blank=True, null=True, verbose_name='Do')),
                ('clan', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hvk.Clan', verbose_name='Član')),
                ('prestanak_cl', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='kat.PrestanakCl', verbose_name='Razlog prestanka')),
                ('vrsta_clanstva', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='kat.VrstaClanstva', verbose_name='Vrsta članstva')),
            ],
            options={
                'ordering': ['-dat_od'],
                'verbose_name_plural': 'Povijest članstva',
                'verbose_name': 'Članstvo',
            },
        ),
    ]
