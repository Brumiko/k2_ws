from django.conf import settings
import requests


def from_mup_get_osoba(oib):
    """
    Prema:
        https://simpleisbetterthancomplex.com/tutorial/2018/02/03/how-to-use-restful-apis-with-django.html
        https://stackoverflow.com/questions/30259452/proper-way-to-consume-data-from-restful-api-in-django#30312778
    :param oib: OIB osobe
    :return: Podaci o osobi u JSON formatu.
    """
    url = settings.J2I_MUP
    return requests.get(url % oib)
