from django.conf import settings
from django.db import models
from kat.models.prestanak_cl import PrestanakCl
from kat.models.vrsta_clanstva import VrstaClanstva


class Clanstvo(models.Model):
    clan = models.ForeignKey('Clan', on_delete=models.DO_NOTHING, verbose_name='Član', )
    vrsta_clanstva = models.ForeignKey(VrstaClanstva, on_delete=models.DO_NOTHING, verbose_name='Vrsta članstva', )
    prestanak_cl = models.ForeignKey(
        PrestanakCl,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        verbose_name='Razlog prestanka')
    dat_od = models.DateField('Od', )
    dat_do = models.DateField('Do', null=True, blank=True, )

    class Meta:
        ordering = ['-dat_od']
        verbose_name = 'Članstvo'
        verbose_name_plural = 'Povijest članstva'

    def __str__(self):
        return '{0} - {1}'.format(
            self.dat_od.strftime('%Y-%m-%d'),
            settings.HVK_PRAZAN_DAT_DO if self.dat_do is None else self.dat_do.strftime('%Y-%m-%d'))
