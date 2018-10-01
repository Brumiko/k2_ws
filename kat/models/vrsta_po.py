from django.db import models


class VrstaPO(models.Model):
    ozn = models.CharField('Oznaka', primary_key=True, max_length=4, )
    naziv = models.CharField('Naziv', max_length=40, unique=True, )

    class Meta:
        db_table = 'kat_vrsta_po'
        ordering = ['naziv', ]
        verbose_name = 'Vrsta pravne osobe'
        verbose_name_plural = 'Vrste pravne osobe'

    def __str__(self):
        return self.naziv

    def save(self, *args, **kwargs):
        self.ozn = self.ozn.lower().strip()
        super(VrstaPO, self).save(*args, **kwargs)
