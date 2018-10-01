from hvk.models.mjesnost_cl import MjesnostCl
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class MjesnostClSerializr(ModelSerializer):
    vrsta_value = SerializerMethodField()
    mjesto_detail = SerializerMethodField()

    class Meta:
        model = MjesnostCl
        fields = ('vrsta', 'vrsta_value', 'mjesto', 'mjesto_detail', 'adresa', )
        read_only_fields = ('vrsta', 'mjesto', 'adresa', )

    @staticmethod
    def get_vrsta_value(obj):
        return obj.vrsta.naziv

    @staticmethod
    def get_mjesto_detail(obj):
        return {
            'mjesto_naziv': obj.mjesto.naziv,
            'mjesto_pbr': obj.mjesto.pbr,
            'mjesto_opcina': obj.mjesto.opcina_id,
            'mjesto_opcina_value': obj.mjesto.opcina.naziv,
            'mjesto_zupanija': obj.mjesto.opcina.zupanija_id,
            'mjesto_zupanija_value': obj.mjesto.opcina.zupanija.naziv,
        }