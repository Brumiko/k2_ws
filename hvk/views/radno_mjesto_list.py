from hvk.models.clan import Clan
from hvk.models.radno_mjesto import RadnoMjesto
from hvk.permissions import IsOwner
from hvk.serializers.radno_mjesto_serializr import RadnoMjestoSerializr
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated


class RadnoMjestoList(ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsOwner,)
    serializer_class = RadnoMjestoSerializr

    def get_queryset(self):
        if self.kwargs['username'] != self.request.user.username:
            raise PermissionDenied('Zabranjeni su pregled i ažuriranje tuđih podataka!')
        return RadnoMjesto.objects.filter(clan__py_user=self.request.user)

    def perform_create(self, serializer):
        clan = Clan.objects.get(py_user=self.request.user)
        serializer.save(clan=clan)