from hvk.models.radno_mjesto import RadnoMjesto
from rest_framework.reverse import reverse_lazy
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class RadnoMjestoSerializr(ModelSerializer):
    links = SerializerMethodField()
    nkz_value = SerializerMethodField()
    po_detail = SerializerMethodField()

    class Meta:
        model = RadnoMjesto
        fields = ('id', 'nkz', 'nkz_value', 'po', 'po_detail', 'dat_od', 'dat_do', 'links', )
        read_only_fields = ('id', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse_lazy('radno_mjesto_solo', kwargs={'username': request.user.username, 'id': obj.id, }, request=request),
        }

    @staticmethod
    def get_nkz_value(obj):
        return obj.nkz.naziv

    @staticmethod
    def get_po_detail(obj):
        return {
            'po_naziv': obj.po.naziv,
            'po_oib': obj.po.oib,
            'po_ziro': obj.po.ziro,
            'po_vrsta': obj.po.vrsta.ozn,
            'po_vrsta_value': obj.po.vrsta.naziv,
        }
