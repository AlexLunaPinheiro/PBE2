from rest_framework import serializers
from .models import Livro, Autor, Editora
from django.contrib.auth.models import User


class AutorSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Autor
        fields = ['id','nome','sobrenome','data_nasc','nacionalidade','biografia']


class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"

class LivroSerializer(serializers.ModelSerializer):

    autor = AutorSerializer(read_only=True)
    editora = EditoraSerializer(read_only=True)
    class Meta:
        model = Livro
        fields = ['id','titulo', 'subtitulo','autor','editora', 'isbn', 'descricao', 'idioma', 'ano', 'paginas','preco',
                  'estoque','desconto', 'disponivel','dimensoes', 'peso', 'capa']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validate_data):
        user = User.objects.create_user(
            username = validate_data['username'],
            password = validate_data['password']
        )

        return user
        

