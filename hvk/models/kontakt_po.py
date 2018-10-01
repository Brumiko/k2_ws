from django.db import models
from kat.models.vrsta_kontakta import VrstaKontakta
from .pravna_osoba import PravnaOsoba


class KontaktPO(models.Model):
    po = models.ForeignKey(PravnaOsoba, on_delete=models.DO_NOTHING, verbose_name='Pravna osoba', )
    vrsta = models.ForeignKey(VrstaKontakta, on_delete=models.DO_NOTHING, verbose_name='Vrsta', )
    sadrzaj = models.CharField('Kontakt', max_length=80, )

    class Meta:
        db_table = 'hvk_kontakt_po'
        ordering = ['vrsta', ]
        unique_together = (('po', 'vrsta', 'sadrzaj', ), )
        verbose_name = 'Kontakt'
        verbose_name_plural = 'Kontakti'

    def __str__(self):
        return self.vrsta.naziv
