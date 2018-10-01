from hvk.models.clanstvo import Clanstvo
from hvk.permissions import IsOwner
from hvk.serializers.clanstvo_serializr import ClanstvoSerializr
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


class ClanstvoList(ListAPIView):
    permission_classes = (IsAuthenticated, IsOwner,)
    serializer_class = ClanstvoSerializr

    def get_queryset(self):
        if self.kwargs['username'] != self.request.user.username:
            raise PermissionDenied('Zabranjeni su pregled i ažuriranje tuđih podataka!')
        return Clanstvo.objects.filter(clan__py_user=self.request.user)
