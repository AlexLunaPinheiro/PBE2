from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import  Autor
from api.serializers import AutorSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from api.filters import AutorFilter

class AutorView(APIView): 
    permission_classes = [AllowAny]
    
    def get(self,request, pk=None):
        filter_backends = [DjangoFilterBackend,SearchFilter]
        filterset_class = AutorFilter
        search_fields = ['nome', 'nacionalidade'] 
        if pk:
            try:
                item = Autor.objects.get(pk=pk)
                serializer = AutorSerializer(item)
                return Response (serializer.data)
                
            except:
                return Response("Autor não encontrado")
            
        else:
            queryset = Autor.objects.all()
            filterset = AutorFilter(request.GET, queryset=queryset)
            if filterset.is_valid():
                queryset = filterset.qs
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