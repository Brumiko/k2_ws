from django.contrib import admin
from kat.models import Zupanija


@admin.register(Zupanija)
class ZupanijaAdmin(admin.ModelAdmin):
    list_display = ('ozn', 'naziv', )
