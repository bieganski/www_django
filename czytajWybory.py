import csv
from pkw.models import Wybory
 
with open('pkw2000.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        wyb = Wybory(wojewodztwo       = row['Województwo'],
                          okrag        = row['Nr okręgu'],
                          kod_gminy    = row['Kod gminy'],
                          gmina        = row['Gmina'],
                          powiat       = row['Powiat'],
                          obwody       = row['Obwody'],                          
                          uprawnieni   = row['Uprawnieni'],
                          wydane       = row['Karty wydane'],
                          oddane       = row['Głosy oddane'],
                          niewazne     = row['Głosy nieważne'],
                          wazne        = row['Głosy ważne'],
                          grabowski    = row['Dariusz Maciej GRABOWSKI'],
                          ikonowicz    = row['Piotr IKONOWICZ'],
                          kalinowski   = row['Jarosław KALINOWSKI'],
                          korwin       = row['Janusz KORWIN-MIKKE'],
                          krzaklewski  = row['Marian KRZAKLEWSKI'],
                          kwasniewski  = row['Aleksander KWAŚNIEWSKI'],
                          lepper       = row['Andrzej LEPPER'],
                          lopuszanski  = row['Jan ŁOPUSZAŃSKI'],
                          olechowski   = row['Andrzej Marian OLECHOWSKI'],
                          pawlowski    = row['Bogdan PAWŁOWSKI'],
                          walesa       = row['Lech WAŁĘSA'],
                          wilecki      = row['Tadeusz Adam WILECKI'])
        wyb.save()

