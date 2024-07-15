from django.db import models

# Create your models here.
class PatologiaTable(models.Model):
    name = models.CharField(max_length=100)
    criticita = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    