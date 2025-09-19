from rest_framework.response import Response
from rest_framework import status
from api.serializers import RegisterSerializer
from rest_framework.permissions import  AllowAny
from rest_framework import viewsets
from django.contrib.auth.models import User


class RegisterViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    permission_classes = [AllowAny]

    def create(self, request): 
        serializer = RegisterSerializer(data = request.data)
        user = serializer
        if serializer.is_valid():
            user.save()
            return Response("usuaário criado com sucesso",status = status.HTTP_201_CREATED)
        else:
            return Response("erro: ",status = status.HTTP_400_BAD_REQUEST)
