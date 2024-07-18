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
