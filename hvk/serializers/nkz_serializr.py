from kat.models.nkz import Nkz
from rest_framework.serializers import ModelSerializer


class NKZSerializr(ModelSerializer):
    class Meta:
        model = Nkz
        fields = ('ozn', 'naziv', )
        read_only_fields = ('ozn', 'naziv', )
