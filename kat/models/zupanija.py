from django.db import models


class Zupanija(models.Model):
    ozn = models.IntegerField('Oznaka', primary_key=True, )
    naziv = models.CharField('Naziv', max_length=50, unique=True, )

    class Meta:
        ordering = ['naziv', ]
        verbose_name = 'Županija'
        verbose_name_plural = 'Županije'

    def __str__(self):
        return self.naziv
