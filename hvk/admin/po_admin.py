from django.contrib import admin
from hvk.models import PravnaOsoba
from .po_inlines import DjelatnostInline, KontaktPoInline, MjesnostPoInline, RadnoMjestoInline


@admin.register(PravnaOsoba)
class PravnaOsobaAdmin(admin.ModelAdmin):
    list_display = ('naziv', 'oib', 'vrsta', )
    list_display_links = ('naziv', )
    search_fields = ('oib', 'naziv', )
    inlines = [DjelatnostInline, KontaktPoInline, MjesnostPoInline, RadnoMjestoInline, ]
    fieldsets = (
        ('Osnovni podaci', {
            'classes': ('suit-tab', 'suit-tab-hvk_osnovno', ),
            'fields': ['naziv', 'oib', 'vrsta', 'ziro', ],
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
            'classes': ('suit-tab', 'suit-tab-hvk_rmj', ),
            'fields': [],
        }),
    )
    suit_form_tabs = (
        ('hvk_osnovno', 'Osnovno'),
        ('hvk_kontakt', 'Kontakt'),
        ('hvk_rmj', 'Radna mjesta')
    )
