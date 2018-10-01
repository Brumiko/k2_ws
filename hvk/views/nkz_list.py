from django.conf import settings
from django.db.models import Q
from hvk.serializers.nkz_serializr import NKZSerializr
from kat.models.nkz import Nkz
from rest_framework.exceptions import NotAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


class NKZList(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = NKZSerializr

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            # return Nkz.objects.none()
            raise NotAuthenticated('Niste ovlašteni za uvid u katalog NKZ.')
        return \
            Nkz.objects.filter(
                Q(
                    naziv__icontains=self.request.query_params['find']
                ) |
                Q(
                    ozn__startswith=self.request.query_params['find']
                )
            )[:settings.HVK_AUTOCOMPLETE_RECORD_COUNT]
