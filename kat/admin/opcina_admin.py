from django.contrib import admin
from kat.models import Opcina


@admin.register(Opcina)
class OpcinaAdmin(admin.ModelAdmin):
    list_display = ('ozn', 'naziv', 'zupanija', )
    search_fields = ['naziv', ]
