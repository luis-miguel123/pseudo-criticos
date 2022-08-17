from django.db import models

# Create your models here.


class User(Base):
    email = models.EmailField("E-mail", max_length=100)
    password = models.CharField("Senha", max_length=20)
    
    def __str__(self):
        return self.email