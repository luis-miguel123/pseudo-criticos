from asyncio.windows_events import NULL
from email.policy import default
from tabnanny import verbose
from django.db import models
from datetime import datetime

# https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbVZZWnRVaXRoel84OGM2eUxyWVREZnl0UGloUXxBQ3Jtc0tubDFLMVJhaU1XZXhTOHRyQTdHZG43T0s1eGpIM1ZWeDlDdkJZNGUteXpOVzkxVjJ5bU5URml6SDdlOEI1RVRkQlotdE1SVG9ocWhFcGtvU19ueE9JZGRYTW5FQmRySGtKVDFrWEMyRGRhczA4XzQycw&q=https%3A%2F%2Fdocs.djangoproject.com%2Fpt-br%2F2.2%2Fref%2Fmodels%2Ffields%2F%23field-types&v=0oWp2WurwyE

# Create your models here.

class Critico(models.Model):
    nome = models.CharField("Crítico", max_length=100)
    senha = models.CharField("Senha", max_length=8)
    data_de_criacao = models.DateTimeField(default=datetime.now())



    def __str__(self):
        return "{} [{}]".format(self.nome, self.id)
    
        

class Avaliacao(models.Model):
    texto = models.CharField(max_length=1000)
    critico = models.ForeignKey(Critico, on_delete=models.PROTECT, verbose_name="Crítico")

    def __str__(self):
        return "{} ({}) [{}]".format(self.texto, self.critico.nome, self.critico.id)
