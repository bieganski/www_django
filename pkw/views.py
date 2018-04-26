from django.shortcuts import render
from pkw.models import Wybory, Kandydat, Okregi
from django.http import Http404
from django.db.models import * # aggregates

from . import utility


def kraj(request):
    ile_wszystkich = Wybory.objects.aggregate(sum=Sum('wazne'))['sum']
    statystyki_ogolne = utility.daj_statystyki_ogolne('kraj', 'cokolwiek')
    statystyki_kandydatow = utility.daj_statystyki_kandydatow('kraj', 'cokolwiek', ile_wszystkich)
    lista_linkow = set([])
    for el in Wybory.objects.all():
        lista_linkow.add(el.wojewodztwo)
    frekwencja = utility.daj_frekwencje_wojewodztw()
    return render(request, 'pkw/kraj.html', {
        'ile_wszystkich': ile_wszystkich,
        'stat_ogolne': statystyki_ogolne,
        'stat_kandydatow': statystyki_kandydatow,
        'lista_linkow': lista_linkow,
        'frekwencja': frekwencja,
    })

def woj(request, wojewodztwo):
    wojewodztwo = wojewodztwo.upper()
    wybory = Wybory.objects.filter(wojewodztwo=wojewodztwo)
    ile_wszystkich = wybory.aggregate(sum=Sum('wazne'))['sum']
    if ile_wszystkich is None:
        raise Http404
    numery_okregow = set([])
    for el in wybory:
        numery_okregow.add(el.okreg.__str__())
    lista_linkow = [{'nr': el, 'nazwa': Okregi.objects.get(pk=el).nazwa} for el in numery_okregow]
    statystyki_ogolne = utility.daj_statystyki_ogolne('wojewodztwo', wojewodztwo)
    statystyki_kandydatow = utility.daj_statystyki_kandydatow('wojewodztwo', wojewodztwo, ile_wszystkich)
    return render(request, 'pkw/woj.html', {
        'wojewodztwo': wojewodztwo,
        'ile_wszystkich': ile_wszystkich,
        'stat_ogolne': statystyki_ogolne,
        'stat_kandydatow': statystyki_kandydatow,
        'lista_linkow': lista_linkow,
    })


def okreg(request, wojewodztwo, okreg):
    wybory = Wybory.objects.filter(okreg=okreg)
    ile_wszystkich = wybory.aggregate(sum=Sum('wazne'))['sum']
    if ile_wszystkich is None:
        raise Http404
    statystyki_ogolne = utility.daj_statystyki_ogolne('okreg', okreg)
    statystyki_kandydatow = utility.daj_statystyki_kandydatow('okreg', okreg, ile_wszystkich)
    lista_gmin = set([])
    for el in wybory:
        lista_gmin.add(el.gmina)
    return render(request, 'pkw/okreg.html', {
        'wojewodztwo': wojewodztwo,
        'okreg': okreg,
        'ile_wszystkich': ile_wszystkich,
        'stat_ogolne': statystyki_ogolne,
        'stat_kandydatow': statystyki_kandydatow,
        'lista_linkow': list(lista_gmin),
    })

def gmina(request, wojewodztwo, okreg, gmina):
    gmina = gmina.title()
    ile_wszystkich = Wybory.objects.filter(okreg=okreg). \
        filter(gmina=gmina.title()). \
        aggregate(sum=Sum('wazne'))['sum']
    if ile_wszystkich is None:
        raise Http404
    statystyki_ogolne = utility.daj_statystyki_ogolne('gmina', gmina)
    statystyki_kandydatow = utility.daj_statystyki_kandydatow('gmina', gmina, ile_wszystkich)
    return render(request, 'pkw/gmina.html', {
        'wojewodztwo': wojewodztwo,
        'okreg': okreg,
        'gmina': gmina,
        'ile_wszystkich': ile_wszystkich,
        'stat_ogolne': statystyki_ogolne,
        'stat_kandydatow': statystyki_kandydatow,
    })
