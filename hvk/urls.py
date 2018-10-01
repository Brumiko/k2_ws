from django.conf.urls import url
from hvk.views import \
    ApiRoot, \
    ClanSolo, \
    ClanstvoList, \
    KontaktiClList, KontaktClSolo, \
    MjesnostClList, \
    NKZList, \
    POList, \
    RadnoMjestoList, RadnoMjestoSolo, \
    VrstaClanstvaList, VrstaKontaktaList
from rest_framework.schemas import get_schema_view
from rest_framework.urlpatterns import format_suffix_patterns


schema_view = get_schema_view(title='HVK web-API')

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^clanovi/(?P<username>[\w.@+-]+)/$', ClanSolo.as_view(), name='clan_solo'),
    url(r'^clanovi/(?P<username>[\w.@+-]+)/kontakti/(?P<id>\d+)/$', KontaktClSolo.as_view(), name='kontakt_cl_solo'),
    url(r'^clanovi/(?P<username>[\w.@+-]+)/kontakti/$', KontaktiClList.as_view(), name='kontakt_cl_list'),
    url(r'^clanovi/(?P<username>[\w.@+-]+)/clanstvo/$', ClanstvoList.as_view(), name='clanstvo_list'),
    url(r'^clanovi/(?P<username>[\w.@+-]+)/mjesnost/$', MjesnostClList.as_view(), name='mjesnost_cl_list'),
    url(r'^clanovi/(?P<username>[\w.@+-]+)/radna-mjesta/(?P<id>\d+)/$', RadnoMjestoSolo.as_view(), name='radno_mjesto_solo'),
    url(r'^clanovi/(?P<username>[\w.@+-]+)/radna-mjesta/$', RadnoMjestoList.as_view(), name='radno_mjesto_list'),
    url(r'^autocomplete_nkz/$', NKZList.as_view(), name='autocomplete_nkz'),
    url(r'^autocomplete_po/$', POList.as_view(), name='autocomplete_po'),
    url(r'^vrsta_clanstva/$', VrstaClanstvaList.as_view(), name='list_vrsta_clanstva'),
    url(r'^vrsta_kontakta/$', VrstaKontaktaList.as_view(), name='list_vrsta_kontakta'),
    url(r'^$', ApiRoot.as_view(), name='api_root'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
