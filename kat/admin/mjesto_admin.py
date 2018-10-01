from django.contrib import admin
from kat.models import Mjesto


@admin.register(Mjesto)
class MjestoAdmin(admin.ModelAdmin):
    list_display = ('ozn', 'pbr', 'naziv', 'opcina', )
    search_fields = ('pbr', 'naziv', )
