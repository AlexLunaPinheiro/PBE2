from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Livro
from api.serializers import LivroSerializer
from rest_framework.permissions import IsAuthenticated


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
    