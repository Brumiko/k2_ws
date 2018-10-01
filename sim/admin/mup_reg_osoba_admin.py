from django.contrib import admin
from sim.models.mup_reg_osoba import MUPRegOsoba


@admin.register(MUPRegOsoba)
class MUPRegOsobaAdmin(admin.ModelAdmin):
    list_display = ('oib', 'ime', 'prezime', 'spol', 'dat_rod', )
    search_fields = ('ime', 'prezime', 'oib', )
