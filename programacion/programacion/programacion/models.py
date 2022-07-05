from pyexpat import model
from django.db import models

# Create your models here.
class Programacion(models.Model):
    idmedico = models.IntegerField()
    idconsultorio = models.IntegerField()
    idturno =  models.IntegerField()
    cupos = models.IntegerField()
    minutos = models.TimeField()
    fechaProgramada = models.DateField(null=True)
    estado = models.CharField(max_length=1,default='A')
    class Meta:
        managed = True
        db_table = 'programacion'