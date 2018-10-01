from rest_framework.reverse import reverse_lazy
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class SimRoot(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        data = {
            'simulacija MUP-ovog registra osoba': reverse_lazy('mup_osobe', request=request),
            'prikaz osobe iz MUP-ovog registra': reverse_lazy('mup_osoba_solo', ['_oib_', ], request=request),
        }
        return Response(data)