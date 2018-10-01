from hvk.serializers.vrsta_kontakta_serializr import VrstaKontaktaSerializr
from kat.models.vrsta_kontakta import VrstaKontakta
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


class VrstaKontaktaList(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = VrstaKontaktaSerializr
    queryset = VrstaKontakta.objects.all()
