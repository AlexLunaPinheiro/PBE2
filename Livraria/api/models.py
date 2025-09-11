from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    data_nasc = models.DateField(null = True, blank= True)
    nacionalidade = models.CharField(max_length=50)
    biografia = models.TextField(null=True, blank = True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

class Editora(models.Model):
    editora = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, blank=True, unique=True, null = True)
    endereco = models.CharField(max_length=201, null = True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    site = models.URLField(null=True)

    def __str__(self):
        return f"{self.editora}"

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=50)
    descricao = models.TextField()
    idioma = models.CharField(default="Portugues")
    ano = models.IntegerField()
    paginas = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    desconto = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    dimensoes = models.CharField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    autor = models.ForeignKey(Autor, related_name='livros', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo}"
    