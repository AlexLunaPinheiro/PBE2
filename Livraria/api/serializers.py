from rest_framework import serializers
from .models import Livro, Autor, Editora

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"

class AutorSerializer(serializers.ModelSerializer):
    livros = LivroSerializer(many = True, read_only = True)
    class Meta:
        model = Autor
        fields = ['id','nome','sobrenome','data_nasc','nacionalidade','biografia','livros']


class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"