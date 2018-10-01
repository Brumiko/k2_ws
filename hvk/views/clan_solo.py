from hvk.models.clan import Clan
from hvk.permissions import IsOwner
from hvk.serializers.clan_serializr import ClanSerializr
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


class ClanSolo(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsOwner, )
    serializer_class = ClanSerializr
    lookup_field = 'py_user__username'
    lookup_url_kwarg = 'username'

    def get_queryset(self):
        if self.kwargs['username'] != self.request.user.username:
            raise PermissionDenied('Zabranjeni su pregled i ažuriranje tuđih podataka!')
        return Clan.objects.filter(py_user=self.request.user)

    def perform_update(self, serializer):
        clan = Clan.objects.get(py_user=self.request.user)
        serializer.save(clan=clan)

    def perform_destroy(self, instance):
        # TODO: Podržati brisanje.
        # instance.delete()
        raise Exception('Brisanje člana još nije podržano.')
