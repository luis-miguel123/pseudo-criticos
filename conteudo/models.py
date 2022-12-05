from asyncio.windows_events import NULL
from email.policy import default
from tabnanny import verbose
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Filme(models.Model):
    nome = models.CharField("Nome", max_length=50)
    genero = models.CharField("Genêro", max_length=20)

    def __str__(self):
        return "{} {}".format(self.nome, self.genero)

class Avaliacao(models.Model):
    titulo = models.CharField("Titulo", max_length=50)
    critica = models.CharField("Critica", max_length=250)
    data_de_criacao = models.DateTimeField(default=datetime.now())
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return "titulo : {} | nome do filme : {}".format(self.titulo, self.filme)


    
