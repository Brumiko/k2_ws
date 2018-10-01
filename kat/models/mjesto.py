from django.db import models
from .opcina import Opcina


class Mjesto(models.Model):
    ozn = models.CharField('Oznaka', primary_key=True, max_length=6, )
    opcina = models.ForeignKey(Opcina, on_delete=models.DO_NOTHING, verbose_name='Općina', )
    pbr = models.CharField('Poštanski broj', max_length=5, null=True, )
    naziv = models.CharField('Naziv', max_length=80, )

    class Meta:
        ordering = ['naziv', ]
        verbose_name = 'Mjesto'
        verbose_name_plural = 'Mjesta'

    def __str__(self):
        return '{0} {1}'.format('' if self.pbr is None else self.pbr, self.naziv)
