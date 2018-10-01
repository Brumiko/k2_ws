from hvk.models.pravna_osoba import PravnaOsoba
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class POSerializr(ModelSerializer):
    vrsta_value = SerializerMethodField()

    class Meta:
        model = PravnaOsoba
        fields = ('id', 'vrsta', 'vrsta_value', 'oib', 'naziv', 'ziro', )
        read_only_fields = ('id', 'vrsta', 'oib', 'naziv', 'ziro', )

    @staticmethod
    def get_vrsta_value(obj):
        return obj.vrsta.naziv
