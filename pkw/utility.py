#
# --------- TUTAJ SĄ PRZYDATNE FUNKCJE POMOCNICZE ---------
#

from django.db.models import * # aggregates
from pkw.models import *
from django.http import Http404


def daj_statystyki_kandydatow(nazwa_jednostki, jednostka, ile_wszystkich):
    """
    W danym regionie wylicza statystki kandydatów.
    :param ile_wszystkich: liczba wszystkich ważnych głosów w rejonie.
    :return: zwraca słownik {kandydat, głosy, procentowe poparcie}
    """
    wyniki = Kandydat.objects.values()
    wybory = Wybory.objects.all()

    for kand in wyniki:
        if nazwa_jednostki != 'kraj':
            suma = wybory.filter(**{nazwa_jednostki: jednostka}).aggregate(sum=Sum(kand['skrot']))['sum']
        else:
            suma = wybory.aggregate(sum=Sum(kand['skrot']))['sum']
        kand['suma'] = suma
        kand['procenty'] = round((suma / ile_wszystkich) * 100, 2)
    return wyniki

def daj_statystyki_ogolne(nazwa_jednostki, jednostka):
    lista = Wybory.objects.all()
    if nazwa_jednostki != 'kraj':
        lista = lista.filter(**{nazwa_jednostki: jednostka})
    if not lista:
        raise Http404
    return {
        'uprawnieni': lista.aggregate(sum=Sum('uprawnieni'))['sum'],
        'wydane': lista.aggregate(sum=Sum('wydane'))['sum'],
        'oddane': lista.aggregate(sum=Sum('oddane'))['sum'],
        'wazne': lista.aggregate(sum=Sum('wazne'))['sum'],
        'niewazne': lista.aggregate(sum=Sum('niewazne'))['sum'],
        'frekwencja': round(
            (lista.aggregate(sum=Sum('wydane'))['sum']
             / lista.aggregate(sum=Sum('uprawnieni'))['sum']) * 100, 2),
    }


def daj_frekwencje_wojewodztw():
    """
    Zwraca listę krotek (wojewodztwo, frekwencja)
    """
    wyb = Wybory.objects.all()
    wojewodztwa = set([])
    wyn = []
    for el in wyb:
        wojewodztwa.add(el.wojewodztwo)
    for woj in wojewodztwa:
        ile = wyb.filter(wojewodztwo=woj).aggregate(sum=Sum('wazne'))['sum']
        wyn.append((woj, ile))
    return wyn