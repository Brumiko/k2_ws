from sim.models.mup_reg_osoba import MUPRegOsoba
from rest_framework.reverse import reverse_lazy
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class MUPOsobaSerializr(ModelSerializer):
    links = SerializerMethodField()

    class Meta:
        model = MUPRegOsoba
        fields = ('oib', 'ime', 'prezime', 'spol', 'dat_rod',
                  'preb_ulica_kbr', 'preb_mjesto_sifra', 'preb_mjesto_naziv',
                  'bora_ulica_kbr', 'bora_mjesto_sifra', 'bora_mjesto_naziv',
                  'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse_lazy('mup_osoba_solo', kwargs={'oib': obj.oib}, request=request),
        }
