from django.conf import settings
from django.db.models import Q
from hvk.models.pravna_osoba import PravnaOsoba
from hvk.serializers.po_serializr import POSerializr
from rest_framework.exceptions import NotAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


class POList(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = POSerializr

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            # return PravnaOsoba.objects.none()
            return NotAuthenticated('Niste ovlašteni za uvid u katalog PO.')
        return PravnaOsoba.objects.filter(
            Q(
                naziv__icontains=self.request.query_params['find']
            ) |
            Q(
                oib__startswith=self.request.query_params['find']
            )
        )[:settings.HVK_AUTOCOMPLETE_RECORD_COUNT]
