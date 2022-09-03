from django.db import models

# Create your models here.
class Familiares(models.Model):
    nombre = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()
    peso_kg = models.IntegerField()

    
    


class Datos(models.Model):
    profesion = models.CharField(max_length=128)
    hobbys = models.CharField(max_length=128)