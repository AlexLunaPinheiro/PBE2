from rest_framework import serializers
from .models import Livro, Autor

class LivroSerializer(serializers.ModelSerializer):
    autor_nome = serializers.StringRelatedField(source="autor", read_only=True)
    class Meta:
        model = Livro
        fields = ['id', 'titulo' , 'autor' , 'autor_nome']

class AutorSerializer(serializers.ModelSerializer):
    livros = LivroSerializer(many = True, read_only = True)
    class Meta:
        model = Autor
        fields = ['id','nome','sobrenome','data_nasc','nacionalidade','biografia','livros']

