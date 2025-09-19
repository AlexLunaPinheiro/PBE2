from rest_framework import serializers
from .models import Livro, Autor, Editora
from django.contrib.auth.models import User

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
        

