from django.contrib import admin
from kat.models import VrstaClanstva


@admin.register(VrstaClanstva)
class VrstaClanstvaAdmin(admin.ModelAdmin):
    list_display = ('ozn', 'naziv', )
