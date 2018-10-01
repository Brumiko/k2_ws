from django.db import models
from .obr_razina import ObrRazina


class ObrTitula(models.Model):
    ozn = models.CharField('Kratica', primary_key=True, max_length=40, )  # Dugi nazivi, npr. univ.bacc.biol.et oecol.
    razina = models.ForeignKey(ObrRazina, on_delete=models.DO_NOTHING, verbose_name='Razina', )
    naziv = models.TextField('Puni naziv', max_length=255, unique=True, )

    class Meta:
        db_table = 'kat_obr_titula'
        ordering = ['ozn', ]
        verbose_name = 'Obrazovna titula'
        verbose_name_plural = 'Obrazovne titule'

    def __str__(self):
        return self.ozn

    def save(self, *args, **kwargs):
        self.ozn = self.ozn.lower().strip()
        super(ObrTitula, self).save(*args, **kwargs)
