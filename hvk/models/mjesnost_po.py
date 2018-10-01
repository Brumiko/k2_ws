from django.db import models
from kat.models.mjesto import Mjesto
from kat.models.vrsta_mjesnosti import VrstaMjesnosti
from .pravna_osoba import PravnaOsoba


class MjesnostPO(models.Model):
    po = models.ForeignKey(PravnaOsoba, on_delete=models.DO_NOTHING, verbose_name='Pravna osoba', )
    mjesto = models.ForeignKey(Mjesto, on_delete=models.DO_NOTHING, verbose_name='Mjesto', )
    vrsta = models.ForeignKey(VrstaMjesnosti, on_delete=models.DO_NOTHING, verbose_name='Vrsta', )
    adresa = models.CharField('Ulica i kućni broj', max_length=80, )

    class Meta:
        db_table = 'hvk_mjesnost_po'
        ordering = ['mjesto', ]
        unique_together = (('mjesto', 'po', 'vrsta', ), )
        verbose_name = 'Mjesnost'
        verbose_name_plural = 'Mjesnosti'

    def __str__(self):
        return self.vrsta.naziv
