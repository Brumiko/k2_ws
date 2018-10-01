from django.db import models
from kat.models.nkd import Nkd
from .pravna_osoba import PravnaOsoba


class Djelatnost(models.Model):
    po = models.ForeignKey(PravnaOsoba, on_delete=models.DO_NOTHING, verbose_name='Pravna osoba', )
    nkd = models.ForeignKey(Nkd, on_delete=models.DO_NOTHING, verbose_name='NKD', )
    dat_od = models.DateField('Od', )
    dat_do = models.DateField('Do', null=True, blank=True, )

    class Meta:
        unique_together = (('po', 'nkd'),)
        ordering = ['nkd', ]
        verbose_name = 'Djelatnost'
        verbose_name_plural = 'Djelatnosti'

    def __str__(self):
        return self.nkd.naziv
