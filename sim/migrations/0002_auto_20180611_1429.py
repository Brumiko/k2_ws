# Generated by Django 2.0.5 on 2018-06-11 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mupregosoba',
            options={'ordering': ['prezime', 'ime', '-dat_rod'], 'verbose_name': 'Osoba (sim MUP)', 'verbose_name_plural': 'Osobe (sim MUP)'},
        ),
        migrations.AlterField(
            model_name='mupregosoba',
            name='bora_mjesto_naziv',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Naziv boravišta'),
        ),
        migrations.AlterField(
            model_name='mupregosoba',
            name='bora_mjesto_sifra',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='DGU-šifra boravišta'),
        ),
        migrations.AlterField(
            model_name='mupregosoba',
            name='bora_ulica_kbr',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='Ulica i kbr boravišta'),
        ),
        migrations.AlterField(
            model_name='mupregosoba',
            name='dat_rod',
            field=models.DateField(verbose_name='Dat. rođenja'),
        ),
        migrations.AlterField(
            model_name='mupregosoba',
            name='ime',
            field=models.CharField(max_length=35, verbose_name='Ime'),
        ),
        migrations.AlterField(
            model_name='mupregosoba',
            name='oib',
            field=models.CharField(max_length=13, primary_key=True, serialize=False, verbose_name='OIB'),
        ),
        migrations.AlterField(
            model_name='mupregosoba',
            name='preb_mjesto_naziv',
            field=models.CharField(max_length=32, verbose_name='Naziv prebivališta'),
        ),
        migrations.AlterField(
            model_name='mupregosoba',
            name='preb_mjesto_sifra',
            field=models.CharField(max_length=6, verbose_name='DGU-šifra prebivališta'),
        ),
        migrations.AlterField(
            model_name='mupregosoba',
            name='preb_ulica_kbr',
            field=models.CharField(max_length=45, verbose_name='Ulica i kbr prebivališta'),
        ),
        migrations.AlterField(
            model_name='mupregosoba',
            name='prezime',
            field=models.CharField(max_length=35, verbose_name='Prezime'),
        ),
        migrations.AlterField(
            model_name='mupregosoba',
            name='spol',
            field=models.CharField(max_length=1, verbose_name='Spol'),
        ),
    ]
