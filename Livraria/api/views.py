from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Livro, Autor
from .serializers import LivroSerializer, AutorSerializer

class LivroListCreate(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


class LivroRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


class AutorListCreate(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class AutorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


@api_view(['GET','POST'])
def criarLivro(request):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer(queryset, many = True)

    if request.method == "GET":
        return Response(serializer_class.data)
    
    if request.method == "POST":
        serializer_class = LivroSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
            
@api_view(['GET'])
def listarAutores(request):
    if request.method == "GET":
        queryset = Autor.objects.all()
        serializer = AutorSerializer(queryset,many = True)
        return Response(serializer.data)


@api_view(['POST'])
def criarAutor(request):
    serializer = AutorSerializer(data = request.data)
    if request.method == "POST":
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        

@api_view(['GET','POST','PUT','DELETE'])
def listarLivros(request, pk):

    item = Livro.objects.get(pk=pk)
    if request.method == "GET":
        serializer = LivroSerializer(item)
        return Response(serializer.data)
    
    elif request.method == "PUT":
    
        serializer = LivroSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    elif request.method == "DELETE":
        item.delete()
        return Response(status=status.HTTP_200_OK)


    

        
        


