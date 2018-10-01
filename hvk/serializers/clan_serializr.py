from django.contrib.auth.models import User
from hvk.models.clan import Clan
from rest_framework.reverse import reverse_lazy
from rest_framework.serializers import ModelSerializer, SerializerMethodField, SlugRelatedField


class ClanSerializr(ModelSerializer):
    links = SerializerMethodField()
    py_user = SlugRelatedField(slug_field=User.USERNAME_FIELD, read_only=True, )

    class Meta:
        model = Clan
        fields = ('py_user', 'oib', 'spol', 'dat_rod', 'slika', 'ime', 'prezime', 'aktivno_clanstvo', 'email', 'links', )
        read_only_fields = ('oib', 'spol', 'dat_rod', 'ime', 'prezime', 'aktivno_clanstvo', 'email', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse_lazy('clan_solo', kwargs={'username': request.user.username, }, request=request),
            'članstvo': reverse_lazy('clanstvo_list', kwargs={'username': request.user.username, }, request=request),
            'kontakti': reverse_lazy('kontakt_cl_list', kwargs={'username': request.user.username, }, request=request),
            'mjesnosti': reverse_lazy('mjesnost_cl_list', kwargs={'username': request.user.username, }, request=request),
            'radna mjesta': reverse_lazy('radno_mjesto_list', kwargs={'username': request.user.username, }, request=request)
        }
