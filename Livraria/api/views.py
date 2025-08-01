from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Bibliotecario

class ListarBibliotecario(APIView):
    def get(self, request):
        listaBibliotecarios = Bibliotecario.nome
        return Response(listaBibliotecarios)