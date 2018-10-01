from django.contrib import admin
from kat.models import ObrTitula


@admin.register(ObrTitula)
class ObrTitulaAdmin(admin.ModelAdmin):
    list_display = ('ozn', 'razina', 'naziv', )
    search_fields = ['ozn', 'naziv', ]
