from django.db import models
from kat.models.nkz import Nkz
from .clan import Clan
from .pravna_osoba import PravnaOsoba


class RadnoMjesto(models.Model):
    nkz = models.ForeignKey(Nkz, on_delete=models.DO_NOTHING, verbose_name='Zvanje po NKZ', )
    po = models.ForeignKey(PravnaOsoba, on_delete=models.DO_NOTHING, verbose_name='Pravna osoba', )
    clan = models.ForeignKey(Clan, on_delete=models.DO_NOTHING, verbose_name='Radnik (član HVK)', )
    dat_od = models.DateField('Od', )
    dat_do = models.DateField('Do', null=True, blank=True, )

    class Meta:
        db_table = 'hvk_radno_mjesto'
        ordering = ['-dat_od', ]
        verbose_name = 'Radno mjesto'
        verbose_name_plural = 'Radna mjesta'

    def __str__(self):
        return '{0} @ {1}'.format(self.nkz.ozn, self.po.naziv)
