from django.db import models
from kat.models.vrsta_po import VrstaPO


class PravnaOsoba(models.Model):
    vrsta = models.ForeignKey(VrstaPO, on_delete=models.DO_NOTHING, verbose_name='Vrsta', )
    oib = models.CharField('OIB', max_length=13, unique=True, )
    naziv = models.CharField('Naziv', max_length=80, )
    ziro = models.CharField('Žiro-račun', max_length=21, )

    class Meta:
        db_table = 'hvk_pravna_osoba'
        ordering = ['naziv', ]
        verbose_name = 'Pravna osoba'
        verbose_name_plural = 'Pravne osobe'

    def __str__(self):
        return '{0}, {1}'.format(self.naziv, self.oib)
