from django.conf.urls import url
from sim.views import SimRoot, MUPOsobe, MUPOsobaSolo


urlpatterns = [
    url(r'^mup-osobe/(?P<oib>[\w.@+-]+)/$', MUPOsobaSolo.as_view(), name='mup_osoba_solo'),
    url(r'^mup-osobe/$', MUPOsobe.as_view(), name='mup_osobe'),
    url(r'^$', SimRoot.as_view(), name='sim_root'),
]
