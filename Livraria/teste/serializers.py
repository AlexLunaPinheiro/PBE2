from rest_framework import serializers
from .models import Autor

class AutorSerializer(serializers.Serializer):
    nome = serializers.CharField(required = True)
    sobrenome = serializers.CharField(required = True)
    
    def create(self,validated_data):
        return Autor.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome',instance.nome)
        instance.sobrenome = validated_data.get('sobrenome',instance.sobrenome)
        instance.save()
        return instance
    

