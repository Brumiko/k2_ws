from django.db import models
from kat.models.vrsta_kontakta import VrstaKontakta
from .clan import Clan


class KontaktCl(models.Model):
    clan = models.ForeignKey(Clan, on_delete=models.DO_NOTHING, verbose_name='Član', )
    vrsta = models.ForeignKey(VrstaKontakta, on_delete=models.DO_NOTHING, verbose_name='Vrsta', )
    sadrzaj = models.CharField('Kontakt', max_length=80, )

    class Meta:
        db_table = 'hvk_kontakt_cl'
        ordering = ['vrsta', ]
        unique_together = (('clan', 'vrsta', 'sadrzaj', ), )
        verbose_name = 'Kontakt'
        verbose_name_plural = 'Kontakti'

    def __str__(self):
        return self.vrsta.naziv
