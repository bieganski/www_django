import csv
from pkw.models import Kandydat
 
with open('kandydaci.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        kand = Kandydat(skrot = row['SKROT'], pelna_godnosc = row['PELNA_GODNOSC'])
        kand.save()
