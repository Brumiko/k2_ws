from django.db import models
from .zupanija import Zupanija


class Opcina(models.Model):
    ozn = models.CharField('DGU oznaka', primary_key=True, max_length=5, )
    zupanija = models.ForeignKey(Zupanija, on_delete=models.DO_NOTHING, verbose_name='Županija', )
    naziv = models.CharField('Naziv', max_length=80, )

    class Meta:
        ordering = ['naziv', ]
        verbose_name = 'Općina'
        verbose_name_plural = 'Općine'

    def __str__(self):
        return self.naziv
