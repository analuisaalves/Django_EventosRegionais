from django.db import models

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=255)
    data = models.DateField()

    def __str__(self):
        return f'{self.titulo} {self.data}'