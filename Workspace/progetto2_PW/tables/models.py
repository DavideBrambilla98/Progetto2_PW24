import random
import string

from django.db import models

# Create your models here.
class PatologiaTable(models.Model):
    codice = models.CharField(max_length=10)
    nome = models.CharField(max_length=120)
    criticita = models.CharField(max_length=20)
    cronica = models.CharField(max_length=1)
    mortale = models.CharField(max_length=1)

    def __str__(self):
        return self.nome # serve per nominare le tabelle nel DB

class CittadinoTable(models.Model):
        cognome = models.CharField(max_length=20)
        nome = models.CharField(max_length=20)
        nasLuogo = models.CharField(max_length=20)
        nasRegione = models.CharField(max_length=20)
        nasProv = models.CharField(max_length=4)
        nasCap = models.CharField(max_length=7)
        dataNascita = models.DateField()
        codFiscale = models.CharField(max_length=50)
        resLuogo = models.CharField(max_length=50)
        resRegione = models.CharField(max_length=50)
        resProv = models.CharField(max_length=4)
        resCap = models.CharField(max_length=7)
        indirizzo = models.CharField(max_length=60)
        def __str__(self):
            return self.codFiscale  # serve per nominare le tabelle nel DB

class OspedaleTable(models.Model):
    codiceStruttura = models.CharField(max_length=10)
    denominazioneStruttura = models.CharField(max_length=50)
    indirizzo = models.CharField(max_length=50)
    comune = models.CharField(max_length=50)
    descrizioneTipoStruttura = models.CharField(max_length=50)
    direttoreSanitario = models.ForeignKey(CittadinoTable, on_delete=models.CASCADE)

    def __str__(self):
        return self.denominazioneStruttura # serve per nominare le tabelle nel DB

class RicoveroTable(models.Model):
    codiceOspedale = models.ForeignKey(OspedaleTable, on_delete=models.CASCADE)
    codiceRicovero = models.CharField(max_length=20, unique=True)
    paziente = models.ForeignKey(CittadinoTable, on_delete=models.CASCADE)
    data = models.DateField()
    durata = models.IntegerField()
    motivo = models.CharField(max_length=50)
    costo = models.IntegerField()

class PatologiaRicoveroTable(models.Model):
    codOspedale = models.ForeignKey(OspedaleTable, on_delete=models.CASCADE)
    codRicovero = models.ForeignKey(RicoveroTable, on_delete=models.CASCADE)
    codPatologia = models.ForeignKey(PatologiaTable, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.codRicovero)  # serve per nominare le tabelle nel DB