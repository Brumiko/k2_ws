from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.utils.safestring import mark_safe
from .clanstvo import Clanstvo
import datetime
import os


class Clan(models.Model):
    SPOL = (
        ('m', 'muško'),
        ('f', 'žensko')
    )
    py_user = models.OneToOneField(User, on_delete=models.DO_NOTHING, verbose_name='Korisničko ime', )
    oib = models.CharField('OIB', max_length=13, unique=True, null=True, blank=True, )
    spol = models.CharField('Spol', choices=SPOL, max_length=1, null=True, blank=True, )
    dat_rod = models.DateField('Datum rođenja', null=True, blank=True, )
    slika = models.ImageField('Slika', upload_to=settings.HVK_CLAN_FOTO_PATH, max_length=255, null=True, blank=True, )
    ime = models.CharField('Ime', max_length=35, null=True, blank=True, )
    prezime = models.CharField('Prezime', max_length=35, null=True, blank=True, )

    class Meta:
        ordering = ['prezime', 'ime', 'dat_rod']
        verbose_name = 'Član'
        verbose_name_plural = 'Članovi'

    def __str__(self):
        if self.prezime and self.ime and self.oib:
            return '{0}, {1}, {2}'.format(self.prezime, self.ime, self.oib)
        else:
            return self.py_user.username

    def aktivno_clanstvo(self):  # short_description radi samo BEZ 'property' dekoracije
        aktivno_clanstvo = False
        if Clanstvo.objects.filter(clan=self).exists():
            if Clanstvo.objects.filter(Q(clan=self) & (Q(dat_do__gte=datetime.date.today()) | Q(dat_do__isnull=True))):
                aktivno_clanstvo = True
        return aktivno_clanstvo

    def email(self):
        if self.py_user.email:
            return self.py_user.email
        else:
            return None

    def foto(self):
        if self.slika:
            return mark_safe('<img src="{url}" alt="{alt}" width="{width}" />'.format(
                url=self.slika.url,
                alt=self.py_user.username,
                width=settings.HVK_CLAN_FOTO_WIDTH,
            ))
        else:
            return None

    aktivno_clanstvo.short_description = 'Aktivno članstvo?'
    email.short_description = 'E-adresa'
    foto.short_description = 'Fotografija'

    def save(self, *args, **kwargs):
        # TODO: validacija slike!
        # Ovaj algoritam funkcionira zahvaljujući tome što se slike spremaju u podmapu mape media!
        if self.slika:
            slika_path = self.slika.name.split(os.path.sep)
            # Ako se zaprima NOVA slika...
            if self.slika and len(slika_path) == 1:
                postojanje = self.slika_postoji()
                if postojanje[0]:
                    self.brisi_sliku('oib')
                if postojanje[1]:
                    self.brisi_sliku('uname')
                if self.oib:
                    self.slika.name = '{0}.jpg'.format(self.oib)
                else:
                    self.slika.name = '{0}.jpg'.format(self.py_user.username)
            # Ako je slika ispražnjena ili nije niti postojala...
            elif not self.slika:
                postojanje = self.slika_postoji()
                if postojanje[0]:
                    self.brisi_sliku('oib')
                if postojanje[1]:
                    self.brisi_sliku('uname')
                self.slika = None
        # Ako slika postoji ali nije mijenjana: self.slika and len(slika_path) > 1 - onda ne radi niš.
        super(Clan, self).save(*args, **kwargs)

    def slika_postoji(self):
        slika_exists_as_oib = False
        slika_exists_as_uname = False
        # Provjeri postoji li već slika tog korisnika u formatu: <oib>.jpg
        if os.path.isfile(os.path.join(settings.MEDIA_DIR, settings.HVK_CLAN_FOTO_PATH, '{0}.jpg'.format(self.oib), )):
            slika_exists_as_oib = True
        # Provjeri postoji li već slika tog korisnika u formatu: <py_user.username>.jpg
        if os.path.isfile(
            os.path.join(
                settings.MEDIA_DIR, settings.HVK_CLAN_FOTO_PATH,
                '{0}.jpg'.format(self.py_user.username), )):
            slika_exists_as_uname = True
        return slika_exists_as_oib, slika_exists_as_uname

    def brisi_sliku(self, name_type):
        if name_type == 'oib':
            os.remove(os.path.join(settings.MEDIA_DIR, settings.HVK_CLAN_FOTO_PATH, '{0}.jpg'.format(self.oib), ))
        elif name_type == 'uname':
            os.remove(
                os.path.join(
                    settings.MEDIA_DIR, settings.HVK_CLAN_FOTO_PATH, '{0}.jpg'.format(self.py_user.username), ))
