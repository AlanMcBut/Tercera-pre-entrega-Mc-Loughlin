from django.db import models

class Video(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    tipo_de_gama = models.CharField(max_length=20)
    precio = models.IntegerField(null = True)

    def __str__(self):
        return (f"{self.marca} - {self.modelo}")



class Procesador(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    tipo_de_gama = models.CharField(max_length=20)
    precio = models.IntegerField(null = True)

    def __str__(self):
        return (f"{self.marca} - {self.modelo}")
    

class Mouse(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    tipo_de_gama = models.CharField(max_length=20)
    precio = models.IntegerField(null = True)

    def __str__(self):
        return (f"{self.marca} - {self.modelo}")