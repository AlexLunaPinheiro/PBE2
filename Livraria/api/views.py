from rest_framework import generics
from .models import Livro, Autor
from .serializers import LivroSerializer, AutorSerializer

class LivroListCreate(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


class LivroRetrieve(generics.RetrieveAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


class AutorListCreate(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

