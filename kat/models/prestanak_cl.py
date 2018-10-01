from django.db import models


class PrestanakCl(models.Model):
    ozn = models.CharField('Oznaka', primary_key=True, max_length=4, )
    naziv = models.TextField('Naziv', max_length=40, unique=True, )

    class Meta:
        db_table = 'kat_prestanak_cl'
        ordering = ['naziv', ]
        verbose_name = 'Razlog prestanka članstva'
        verbose_name_plural = 'Razlozi prestanka članstva'

    def __str__(self):
        return self.naziv

    def save(self, *args, **kwargs):
        self.ozn = self.ozn.lower().strip()
        super(PrestanakCl, self).save(*args, **kwargs)
