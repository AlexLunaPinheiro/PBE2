from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import  Editora
from api.serializers import  EditoraSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class EditoraView(APIView):
    permission_classes = [AllowAny]
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