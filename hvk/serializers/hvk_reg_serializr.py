from django.db import transaction
from hvk.services import from_mup_get_osoba
from hvk.models import Clan, MjesnostCl
from kat.models import Mjesto, VrstaClanstva, VrstaMjesnosti
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer


class HVKRegSerializr(RegisterSerializer):
    ime = serializers.CharField(required=True, max_length=35, )
    prezime = serializers.CharField(required=True, max_length=35, )
    oib = serializers.CharField(required=True, max_length=13, )
    # Definicija serijalizatora kao Choice Field razjebava web-klijenta!
    # vrsta_clanstva = serializers.ChoiceField(required=True, choices=VrstaClanstva.objects.all(), initial=None, )
    vrsta_clanstva = serializers.CharField(required=True, max_length=4, )
    slika = serializers.ImageField(required=False, )

    def validate(self, data):
        # Validiraj podatke za auth_user u nadklasi.
        data = super(HVKRegSerializr, self).validate(data=data)

        # Dohvati osobu iz MUP-a.
        osoba_response = from_mup_get_osoba(data['oib'])
        if osoba_response.status_code != 200:
            raise serializers.ValidationError(
                'Nema osobnih podataka za upisani OIB. HTTP kod greške jest {0}'.format(osoba_response.status_code))

        # Ako je dohvat iz MUP-a uspio, pretvori osobine podatke u Python-objekt.
        osoba = osoba_response.json()

        # Validiraj korisničko ime u tablici Clan. Vjerojatno nepotrebno.
        if Clan.objects.filter(oib=osoba['oib']).exists():
            raise serializers.ValidationError(
                'Za OIB {0} je već podnesen zahtjev za članstvo. '.format(osoba['oib']) +
                'Ako ste ga podnijeli vi, onda se ne trebate opet registrirati, ' +
                'nego možete nastaviti raditi tako ' +
                'da se prijavite svojim korisničkim imenom i lozinkom.'
            )

        # Ako su validacije uspješne, dodaj dohvaćene osobne podatke u odgovarajuću kolekciju.
        data['ime'] = osoba['ime']
        data['prezime'] = osoba['prezime']
        data['dat_rod'] = osoba['dat_rod']
        data['spol'] = osoba['spol']
        data['oib'] = osoba['oib']
        data['preb_mjesto_sifra'] = osoba['preb_mjesto_sifra']
        data['preb_ozn'] = 'pre'
        data['preb_adresa'] = osoba['preb_ulica_kbr']
        if osoba['bora_mjesto_sifra']:
            data['bora_mjesto_sifra'] = osoba['bora_mjesto_sifra']
            data['bora_ozn'] = 'bor'
            data['bora_adresa'] = osoba['bora_ulica_kbr']

        # Gotovo.
        return data

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'ime': self.validated_data.get('ime', ''),
            'prezime': self.validated_data.get('prezime', ''),
            'dat_rod': self.validated_data.get('dat_rod', ''),
            'spol': self.validated_data.get('spol', ''),
            'oib': self.validated_data.get('oib', ''),
            # 'vrsta_clanstva': self.validated_data.get('vrsta_clanstva', ''),
            'slika': self.validated_data.get('slika', ''),
            'preb_mjesto_sifra': self.validated_data.get('preb_mjesto_sifra', ''),
            'preb_vrsta': self.validated_data.get('preb_ozn', ''),
            'preb_adresa': self.validated_data.get('preb_ulica_kbr'),
            'bora_mjesto_sifra': self.validated_data.get('bora_mjesto_sifra', ''),
            'bora_vrsta':  self.validated_data.get('bora_ozn', ''),
            'bora_adresa': self.validated_data.get('bora_ulica_kbr', ''),
        }

    def save(self, request):
        # TRANSAKCIJSKI spremi novog člana!
        with transaction.atomic():
            # Korisnik.
            user = super(HVKRegSerializr, self).save(request=request)
            # Član.
            clan = Clan.objects.create(
                py_user=user,
                oib=self.validated_data.get('oib'),
                spol=self.validated_data.get('spol'),
                dat_rod=self.validated_data.get('dat_rod'),
                ime=self.validated_data.get('ime'),
                prezime=self.validated_data.get('prezime'),
                slika=None if self.validated_data.get('slika') is None else self.validated_data.get('slika'),
            )
            clan.save()
            # Prebivalište.
            prebivaliste = MjesnostCl.objects.create(
                clan=clan,
                mjesto=Mjesto.objects.get(ozn=self.validated_data.get('preb_mjesto_sifra')),
                vrsta=VrstaMjesnosti.objects.get(ozn=self.validated_data.get('preb_ozn')),
                adresa=self.validated_data.get('preb_adresa'),
            )
            prebivaliste.save()
            # Boravište.
            if self.validated_data.get('bora_mjesto_sifra'):
                boraviste = MjesnostCl.objects.create(
                    clan=clan,
                    mjesto=Mjesto.objects.get(ozn=self.validated_data.get('bora_mjesto_sifra')),
                    vrsta=VrstaMjesnosti.objects.get(ozn=self.validated_data.get('bora_ozn')),
                    adresa=self.validated_data.get('bora_adresa'),
                )
                boraviste.save()
            # KRAJ TRANSAKCIJE
        return user
