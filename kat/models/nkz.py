from django.db import models


class Nkz(models.Model):
    ozn = models.CharField('Oznaka', primary_key=True, max_length=4, )
    naziv = models.TextField('Naziv', max_length=255, unique=True, )

    class Meta:
        ordering = ['ozn', ]
        verbose_name = 'Zvanje po NKZ'
        verbose_name_plural = 'Zvanja po NKZ'

    def __str__(self):
        return '{0} - {1}'.format(self.ozn, self.naziv)

    def save(self, *args, **kwargs):
        self.ozn = self.ozn.lower().strip()
        super(Nkz, self).save(*args, **kwargs)