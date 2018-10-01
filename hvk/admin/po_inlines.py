from django.contrib import admin
from hvk.models import Djelatnost, KontaktPO, MjesnostPO, RadnoMjesto


"""
OSNOVNO
"""


class DjelatnostInline(admin.StackedInline):
    model = Djelatnost
    extra = 0
    fields = ['nkd', 'dat_od', 'dat_do', ]
    suit_classes = 'suit-tab suit-tab-hvk_osnovno'
    autocomplete_fields = ('nkd', )


"""
KONTAKT
"""


class KontaktPoInline(admin.StackedInline):
    model = KontaktPO
    extra = 0
    fields = ['vrsta', 'sadrzaj']
    suit_classes = 'suit-tab suit-tab-hvk_kontakt'


class MjesnostPoInline(admin.StackedInline):
    model = MjesnostPO
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
    fields = ['nkz', 'clan', 'dat_od', 'dat_do']
    suit_classes = 'suit-tab suit-tab-hvk_rmj'
    autocomplete_fields = ('nkz', 'clan', )
