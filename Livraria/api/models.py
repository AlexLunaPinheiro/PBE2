from django.db import models

class Bibliotecario(models.Model):
    nome = models.CharField(max_length=10)
    registoGeral = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    



