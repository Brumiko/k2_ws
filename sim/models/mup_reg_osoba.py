from django.db import models


class MUPRegOsoba(models.Model):
    oib = models.CharField(primary_key=True, max_length=13, verbose_name='OIB')
    ime = models.CharField(max_length=35, verbose_name='Ime')
    prezime = models.CharField(max_length=35, verbose_name='Prezime')
    spol = models.CharField(max_length=1, verbose_name='Spol')
    dat_rod = models.DateField(verbose_name='Dat. rođenja')
    preb_ulica_kbr = models.CharField(max_length=45, verbose_name='Ulica i kbr prebivališta')
    preb_mjesto_sifra = models.CharField(max_length=6, verbose_name='DGU-šifra prebivališta')
    preb_mjesto_naziv = models.CharField(max_length=32, verbose_name='Naziv prebivališta')
    bora_ulica_kbr = models.CharField(max_length=45, blank=True, null=True, verbose_name='Ulica i kbr boravišta')
    bora_mjesto_sifra = models.CharField(max_length=6, blank=True, null=True, verbose_name='DGU-šifra boravišta')
    bora_mjesto_naziv = models.CharField(max_length=32, blank=True, null=True, verbose_name='Naziv boravišta')

    class Meta:
        db_table = 'sim_mup_reg_osoba'
        ordering = ['prezime', 'ime', '-dat_rod']
        verbose_name = 'Osoba (sim MUP)'
        verbose_name_plural = 'Osobe (sim MUP)'

    def __str__(self):
        return '{0}, {1}, {2}'.format(self.prezime, self.ime, self.oib)
