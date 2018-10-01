from django.db import models


class VrstaKontakta(models.Model):
    ozn = models.CharField('Oznaka', primary_key=True, max_length=4, )
    naziv = models.CharField('Naziv', max_length=40, unique=True, )

    class Meta:
        db_table = 'kat_vrsta_kontakta'
        ordering = ['naziv', ]
        verbose_name = 'Vrsta kontakta'
        verbose_name_plural = 'Vrste kontakta'

    def __str__(self):
        return self.naziv

    def save(self, *args, **kwargs):
        self.ozn = self.ozn.lower().strip()
        super(VrstaKontakta, self).save(*args, **kwargs)