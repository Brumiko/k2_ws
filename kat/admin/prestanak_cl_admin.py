from django.contrib import admin
from kat.models import PrestanakCl


@admin.register(PrestanakCl)
class PrestanakClAdmin(admin.ModelAdmin):
    list_display = ('ozn', 'naziv', )
