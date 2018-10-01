from sim.models.mup_reg_osoba import MUPRegOsoba
from sim.serializers.mup_osoba_serializr import MUPOsobaSerializr
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny


class MUPOsobe(ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = MUPRegOsoba.objects.all()
    serializer_class = MUPOsobaSerializr
