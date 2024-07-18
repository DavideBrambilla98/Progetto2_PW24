from django.db import models

# Create your models here.
class PatologiaTable(models.Model):
    titolo = models.CharField(max_length=100)
    codice = models.CharField(max_length=10)
    nome = models.CharField(max_length=120)
    criticita = models.CharField(max_length=20)
    cronica = models.CharField(max_length=1)
    mortale = models.CharField(max_length=1)
    slug = models.SlugField()

    def __str__(self):
        return self.titolo # serve per nominare le tabelle nel DB
