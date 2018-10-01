from django.contrib import admin
from kat.models import ObrRazina


@admin.register(ObrRazina)
class ObrRazinaAdmin(admin.ModelAdmin):
    list_display = ('ozn', 'naziv', )
