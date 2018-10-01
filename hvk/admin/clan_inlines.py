from django.contrib import admin
from hvk.models.clanstvo import Clanstvo
from hvk.models.kontakt_cl import KontaktCl
from hvk.models.mjesnost_cl import MjesnostCl
from hvk.models.radno_mjesto import RadnoMjesto


"""
OSNOVNO
"""


class ClanstvoInline(admin.StackedInline):
    model = Clanstvo
    extra = 0
    fields = ['vrsta_clanstva', 'dat_od', 'dat_do', 'prestanak_cl', ]
    suit_classes = 'suit-tab suit-tab-hvk_osnovno'


"""
KONTAKT
"""


class KontaktClInline(admin.StackedInline):
    model = KontaktCl
    extra = 0
    fields = ['vrsta', 'sadrzaj']
    suit_classes = 'suit-tab suit-tab-hvk_kontakt'


class MjesnostClInline(admin.StackedInline):
    model = MjesnostCl
    extra = 0
    fields = ['mjesto', 'vrsta', 'adresa', ]
    suit_classes = 'suit-tab suit-tab-hvk_kontakt'
    autocomplete_fields = ('mjesto', )


"""
RADNA MJESTA
"""


class RadnoMjestoInline(admin.StackedInline):
    model = RadnoMjesto
    extra = 0
    fields = ['nkz', 'po', 'dat_od', 'dat_do']
    suit_classes = 'suit-tab suit-tab-hvk_rmj'
    readonly_fields = ['nkz', 'po', 'dat_od', 'dat_do']
