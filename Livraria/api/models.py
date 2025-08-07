from django.db import models



class Autor(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    data_nasc = models.DateField(null = True, blank= True)
    nacionalidade = models.CharField(max_length=50)
    biografia = models.TextField(null=True, blank = True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"


class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, related_name='livros', on_delete=models.CASCADE)
    ano = models.IntegerField()