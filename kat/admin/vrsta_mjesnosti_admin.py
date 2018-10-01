from django.contrib import admin
from kat.models import VrstaMjesnosti


@admin.register(VrstaMjesnosti)
class VrstaMjesnostiAdmin(admin.ModelAdmin):
    list_display = ('ozn', 'naziv', )
