from hvk.models.clan import Clan
from hvk.models.radno_mjesto import RadnoMjesto
from hvk.permissions import IsOwner
from hvk.serializers.radno_mjesto_serializr import RadnoMjestoSerializr
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


class RadnoMjestoSolo(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsOwner,)
    serializer_class = RadnoMjestoSerializr
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        if self.kwargs['username'] != self.request.user.username:
            raise PermissionDenied('Zabranjeni su pregled i ažuriranje tuđih podataka!')
        return RadnoMjesto.objects.filter(clan__py_user=self.request.user)

    def perform_update(self, serializer):
        clan = Clan.objects.get(py_user=self.request.user)
        serializer.save(clan=clan)

    def perform_destroy(self, instance):
        instance.delete()
