from hvk.models.kontakt_cl import KontaktCl
from rest_framework.reverse import reverse_lazy
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class KontaktClSerializr(ModelSerializer):
    links = SerializerMethodField()
    vrsta_value = SerializerMethodField()

    class Meta:
        model = KontaktCl
        fields = ('id', 'vrsta', 'vrsta_value', 'sadrzaj', 'links', )
        read_only_fields = ('id', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse_lazy('kontakt_cl_solo', kwargs={'username': request.user.username, 'id': obj.id, }, request=request),
        }

    @staticmethod
    def get_vrsta_value(obj):
        return obj.vrsta.naziv
