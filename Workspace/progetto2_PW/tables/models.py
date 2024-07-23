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

class RicoveroTable(models.Model):
    codiceOspedale = models.CharField(max_length=10)
    codiceRicovero = models.CharField(max_length=20, unique=True, editable=False)
    paziente = models.CharField(max_length=20)
    data = models.DateField()
    durata = models.IntegerField()
    motivo = models.CharField(max_length=50)
    costo = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.codiceRicovero:
            self.codiceRicovero = self.generate_codiceRicovero()
        super(RicoveroTable, self).save(*args, **kwargs)

    def generate_codiceRicovero(self):
        digit1 = ''.join(random.choices(string.digits, k=3))
        letter = ''.join(random.choices(string.ascii_uppercase, k=4))
        digit2 = ''.join(random.choices(string.digits, k=5))
        return f'{digit1}{letter}{digit2}'
    def __str__(self):
        return self.codiceRicovero # serve per nominare le tabelle nel DB

class OspedaleTable(models.Model):
    codiceStruttura = models.CharField(max_length=10)
    denominazioneStruttura = models.CharField(max_length=50)
    indirizzo = models.CharField(max_length=50)
    comune = models.CharField(max_length=50)
    descrizioneTipoStruttura = models.CharField(max_length=50)
    direttoreSanitario = models.CharField(max_length=20)

    def __str__(self):
        return self.denominazioneStruttura # serve per nominare le tabelle nel DB

class PersoneTable(models.Model):
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

class PatologiaRicoveroTable(models.Model):
    codOspedale = models.ForeignKey(OspedaleTable, on_delete=models.CASCADE)
    codRicovero = models.ForeignKey(RicoveroTable, on_delete=models.CASCADE)
    codPatologia = models.ForeignKey(PatologiaTable, on_delete=models.CASCADE)
    def __str__(self):
        return self.codRicovero  # serve per nominare le tabelle nel DB