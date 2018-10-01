from django.db import models


class ObrRazina(models.Model):
    ozn = models.CharField('Oznaka', primary_key=True, max_length=3, )
    naziv = models.TextField('Naziv', max_length=255, unique=True, )

    class Meta:
        db_table = 'kat_obr_razina'
        ordering = ['ozn', ]
        verbose_name = 'Obrazovna razina'
        verbose_name_plural = 'Obrazovne razine'

    def __str__(self):
        return '{0} - {1}'.format(self.ozn, self.naziv)

    def save(self, *args, **kwargs):
        self.ozn = self.ozn.lower().strip()
        super(ObrRazina, self).save(*args, **kwargs)
