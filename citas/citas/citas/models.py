from multiprocessing import managers
from django.db import models

# Create your models here.


class Citas(models.Model):
    idprogramacion = models.IntegerField()
    historia = models.IntegerField()
    fechacita = models.DateField()
    orden = models.IntegerField()
    hora = models.TimeField()
    estado = models.CharField(max_length=1, default='R')

    class Meta:
        managed = True
        db_table = 'citas'