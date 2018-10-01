from rest_framework.reverse import reverse_lazy
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class ApiRoot(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, format=None):
        data = {
            'javno - vrsta članstva': reverse_lazy('list_vrsta_clanstva', request=request),
            'privatno - član': reverse_lazy('clan_solo', ['username', ], request=request),
            'privatno - NKZ': reverse_lazy('autocomplete_nkz', request=request) + '?find=search_param',
            'privatno - pravna osoba': reverse_lazy('autocomplete_po', request=request) + '?find=search_param',
            'privatno - vrsta kontakta': reverse_lazy('list_vrsta_kontakta', request=request),

        }
        return Response(data)
