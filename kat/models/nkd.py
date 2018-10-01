from django.db import models


class Nkd(models.Model):
    ozn = models.CharField('Oznaka', primary_key=True, max_length=9, )
    naziv = models.TextField('Naziv', max_length=255, unique=True, )

    class Meta:
        ordering = ['ozn', ]
        verbose_name = 'Djelatnost po NKD'
        verbose_name_plural = 'Djelatnosti po NKD'

    def __str__(self):
        return '{0} - {1}'.format(self.ozn, self.naziv)

    def save(self, *args, **kwargs):
        self.ozn = self.ozn.lower().strip()
        super(Nkd, self).save(*args, **kwargs)
