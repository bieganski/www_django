from django.db import models


# NAZWISKO, WOJEWÓDZTWO - upper case
class Wybory(models.Model):
    wojewodztwo = models.CharField(max_length=30)
    okreg = models.IntegerField()
    kod_gminy = models.IntegerField()
    gmina = models.CharField(max_length=30)
    powiat = models.CharField(max_length=30)
    obwody = models.IntegerField()
    uprawnieni = models.IntegerField()
    wydane = models.IntegerField()
    oddane = models.IntegerField()
    niewazne = models.IntegerField()
    wazne = models.IntegerField()

    grabowski = models.IntegerField()
    ikonowicz = models.IntegerField()
    kalinowski = models.IntegerField()
    korwin = models.IntegerField()
    krzaklewski = models.IntegerField()
    kwasniewski = models.IntegerField()
    lepper = models.IntegerField()
    lopuszanski = models.IntegerField()
    olechowski = models.IntegerField()
    pawlowski = models.IntegerField()
    walesa = models.IntegerField()
    wilecki = models.IntegerField()

    def __str__(self):
        return self.gmina + ":" + self.kod_gminy.__str__()

class Kandydat(models.Model):
    skrot = models.CharField(max_length=20, primary_key=True)
    pelna_godnosc = models.CharField(max_length=50)

    def __str__(self):
        return self.skrot + ":" + self.pelna_godnosc

class Okregi(models.Model):
    nr = models.IntegerField(primary_key=True)
    nazwa = models.CharField(max_length=20)

    def __str__(self):
        return self.nazwa