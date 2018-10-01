from kat.models.vrsta_kontakta import VrstaKontakta
from rest_framework.serializers import ModelSerializer


class VrstaKontaktaSerializr(ModelSerializer):
    class Meta:
        model = VrstaKontakta
        fields = ('ozn', 'naziv', )
        read_only_fields = ('ozn', 'naziv', )
