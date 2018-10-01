from hvk.models.clanstvo import Clanstvo
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class ClanstvoSerializr(ModelSerializer):
    vrsta_clanstva_value = SerializerMethodField()
    prestanak_cl_value = SerializerMethodField()

    class Meta:
        model = Clanstvo
        fields = ('vrsta_clanstva', 'vrsta_clanstva_value', 'dat_od', 'dat_do', 'prestanak_cl', 'prestanak_cl_value', )
        read_only_fields = ('vrsta_clanstva', 'dat_od', 'dat_do', 'prestanak_cl', )

    @staticmethod
    def get_vrsta_clanstva_value(obj):
        return obj.vrsta_clanstva.naziv

    @staticmethod
    def get_prestanak_cl_value(obj):
        if obj.prestanak_cl is not None:
            return obj.prestanak_cl.naziv
        else:
            return None
