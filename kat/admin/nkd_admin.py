from django.contrib import admin
from kat.models import Nkd


@admin.register(Nkd)
class NkdAdmin(admin.ModelAdmin):
    list_display = ('ozn', 'naziv', )
    search_fields = ('ozn', 'naziv', )
