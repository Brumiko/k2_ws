from hvk.models.mjesnost_cl import MjesnostCl
from hvk.permissions import IsOwner
from hvk.serializers.mjesnost_cl_serializr import MjesnostClSerializr
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


class MjesnostClList(ListAPIView):
    permission_classes = (IsAuthenticated, IsOwner,)
    serializer_class = MjesnostClSerializr

    def get_queryset(self):
        if self.kwargs['username'] != self.request.user.username:
            raise PermissionDenied('Zabranjeni su pregled i ažuriranje tuđih podataka!')
        return MjesnostCl.objects.filter(clan__py_user=self.request.user)
