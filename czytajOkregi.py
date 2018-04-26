import csv
from pkw.models import Okregi
 
with open('okregi.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
    	okr = Okregi(nr=row['NR'], nazwa=row['NAZWA'])
    	okr.save()

