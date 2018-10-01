from django.contrib import admin
from kat.models import VrstaKontakta


@admin.register(VrstaKontakta)
class VrstaKontaktaAdmin(admin.ModelAdmin):
    list_display = ('ozn', 'naziv', )
