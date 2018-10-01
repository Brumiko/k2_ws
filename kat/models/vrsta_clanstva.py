from django.db import models


class VrstaClanstva(models.Model):
    ozn = models.CharField('Oznaka', primary_key=True, max_length=4, )
    naziv = models.CharField('Naziv', max_length=40, unique=True, )

    class Meta:
        db_table = 'kat_vrsta_clanstva'
        ordering = ['naziv', ]
        verbose_name = 'Vrsta članstva'
        verbose_name_plural = 'Vrste članstva'

    def __str__(self):
        return self.naziv
