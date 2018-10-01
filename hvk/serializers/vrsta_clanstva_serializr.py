from kat.models.vrsta_clanstva import VrstaClanstva
from rest_framework.serializers import ModelSerializer


class VrstaClanstvaSerializr(ModelSerializer):
    class Meta:
        model = VrstaClanstva
        fields = ('ozn', 'naziv', )
        read_only_fields = ('ozn', 'naziv', )
