from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view , permission_classes ##Caso eu queira utilizar api_view
from .models import Livro, Autor, Editora
from .serializers import LivroSerializer, AutorSerializer, EditoraSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class AutorView(APIView): 
    permission_classes = [IsAuthenticated]
    
    

    def get(self,request, pk=None):
        filter_backends = [DjangoFilterBackend,SearchFilter]
        if pk:
            try:
                item = Autor.objects.get(pk=pk)
                serializer = AutorSerializer(item)
                return Response (serializer.data)
                
            except:
                return Response("Autor não encontrado")
            
        else:
            queryset = Autor.objects.all()
            for backend in list(filter_backends):
                queryset = backend().filter_queryset(request, queryset, view=AutorView)
            serializer = AutorSerializer(queryset, many = True)
            return Response(serializer.data)
        
        

    def post(self,request):
        serializer = AutorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("Erro ao criar autor",status.HTTP_404_NOT_FOUND)
        
    def put(self, request,pk=True):
        item = Autor.objects.get(pk=pk)
        serializer = AutorSerializer(item, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk=True):
        item = Autor.objects.get(pk=pk)
        serializer = AutorSerializer(item, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk=True):
        item = Autor.objects.get(pk=pk)
        item.delete()
        return Response(status.HTTP_200_OK)

AutorView.filter_backends = [DjangoFilterBackend, SearchFilter]
AutorView.filterset_fields = ['nacionalidade', 'data_nasc']
AutorView.search_fields = ['nome', 'sobrenome'] 
      

class LivroView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):     
        if pk:
            try:
                item = Livro.objects.get(pk=pk)
                serializer = LivroSerializer(item)
                return Response (serializer.data)
            except:
                return Response("Livro não encontrado")
            
        else:
            queryset = Livro.objects.all()
            serializer = LivroSerializer(queryset, many = True)
            return Response(serializer.data)

    
    def post(self,request):
        serializer = LivroSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:   
            serializer = LivroSerializer(Livro.objects.model())
            return Response(serializer.data,status.HTTP_400_BAD_REQUEST)
        
    def put(self, request,pk=True):
        item = Livro.objects.get(pk=pk)
        serializer = LivroSerializer(item, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status.HTTP_404_NOT_FOUND)
        
    def patch(self, request, pk=True):
        item = Livro.objects.get(pk=pk)
        serializer = LivroSerializer(item, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk=True):
        item = Livro.objects.get(pk=pk)
        item.delete()
        return Response(status.HTTP_200_OK)
    

class EditoraView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):     
        if pk:
            try:
                item = Editora.objects.get(pk=pk)
                serializer = EditoraSerializer(item)
                return Response (serializer.data)
            except:
                return Response("Editora não encontrada")
            
        else:
            queryset = Editora.objects.all()
            serializer = EditoraSerializer(queryset, many = True)
            return Response(serializer.data)

    
    def post(self,request):
        serializer = EditoraSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:   
            serializer = EditoraSerializer(Editora.objects.model())
            return Response(serializer.data,status.HTTP_400_BAD_REQUEST)
        
    def put(self, request,pk=True):
        item = Editora.objects.get(pk=pk)
        serializer = EditoraSerializer(item, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status.HTTP_404_NOT_FOUND)
        
    def patch(self, request, pk=True):
        item = Editora.objects.get(pk=pk)
        serializer = EditoraSerializer(item, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk=True):
        item = Editora.objects.get(pk=pk)
        item.delete()
        return Response(status.HTTP_200_OK)