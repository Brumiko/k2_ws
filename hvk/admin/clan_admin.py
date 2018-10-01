from django.contrib import admin
from hvk.models import Clan
from .clan_inlines import ClanstvoInline, KontaktClInline, MjesnostClInline, RadnoMjestoInline


@admin.register(Clan)
class ClanAdmin(admin.ModelAdmin):
    list_display = ('foto', 'py_user', 'prezime', 'ime', 'oib', 'aktivno_clanstvo', )
    list_display_links = ('py_user', )
    search_fields = ('py_user__username', 'ime', 'prezime', 'oib', )
    autocomplete_fields = ('py_user', )
    readonly_fields = ['foto', 'email', 'aktivno_clanstvo', ]
    inlines = [
        ClanstvoInline,
        KontaktClInline,
        MjesnostClInline,
        RadnoMjestoInline,
    ]
    fieldsets = (
        ('Autentikacija', {
            'classes': ('suit-tab', 'suit-tab-hvk_osnovno', ),
            'fields': ['py_user', 'email', ],
            'description': 'Izvor: \'auth_user\'.',
        }),
        ('Profil', {
            'classes': ('suit-tab', 'suit-tab-hvk_osnovno', ),
            'fields': ['foto', 'slika', 'ime', 'prezime', 'oib', 'spol', 'dat_rod', 'aktivno_clanstvo', ],
            'description': 'Izvor: \'clan\'.',
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-hvk_osnovno', ),
            'fields': [],
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-hvk_kontakt', ),
            'fields': [],
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-hvk_uplata', ),
            'fields': [],
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-hvk_edu', ),
            'fields': [],
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-hvk_napredak', ),
            'fields': [],
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-hvk_rmj', ),
            'fields': [],
        }),
    )
    suit_form_tabs = (
        ('hvk_osnovno', 'Osnovno'),
        ('hvk_kontakt', 'Kontakt'),
        ('hvk_uplata', 'Uplate'),
        ('hvk_edu', 'Obrazovanje'),
        ('hvk_napredak', 'Stručni napredak'),
        ('hvk_rmj', 'Radna mjesta')
    )
