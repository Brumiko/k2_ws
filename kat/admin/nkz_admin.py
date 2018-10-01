from django.contrib import admin
from kat.models import Nkz


@admin.register(Nkz)
class NkzAdmin(admin.ModelAdmin):
    list_display = ('ozn', 'naziv', )
    search_fields = ('ozn', 'naziv', )
