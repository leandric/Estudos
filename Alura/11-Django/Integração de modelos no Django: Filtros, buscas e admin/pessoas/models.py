from pyexpat import model
from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)


    def __str__(self):
        #Ao invés de aparecer o object, aqui setamos para aparecer a propria variavel nome
        return self.nome
    