from hvk.serializers.vrsta_clanstva_serializr import VrstaClanstvaSerializr
from kat.models.vrsta_clanstva import VrstaClanstva
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny


class VrstaClanstvaList(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = VrstaClanstvaSerializr
    queryset = VrstaClanstva.objects.all()
