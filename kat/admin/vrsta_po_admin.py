from django.contrib import admin
from kat.models import VrstaPO


@admin.register(VrstaPO)
class VrstaPoAdmin(admin.ModelAdmin):
    list_display = ('ozn', 'naziv', )
