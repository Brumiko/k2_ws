from django.db import models


class VrstaMjesnosti(models.Model):
    ozn = models.CharField('Oznaka', primary_key=True, max_length=4, )
    naziv = models.CharField('Naziv', max_length=40, unique=True, )

    class Meta:
        db_table = 'kat_vrsta_mjesnosti'
        ordering = ['naziv', ]
        verbose_name = 'Vrsta mjesnosti'
        verbose_name_plural = 'Vrste mjesnosti'

    def __str__(self):
        return self.naziv

    def save(self, *args, **kwargs):
        self.ozn = self.ozn.lower().strip()
        super(VrstaMjesnosti, self).save(*args, **kwargs)
