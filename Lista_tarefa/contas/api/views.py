from rest_framework import generics , permissions
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework import status
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

from django.views.generic import ListView
# from .models import CrudUser
from django.http import JsonResponse


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Criar o token de autenticação
        token = AuthToken.objects.create(user)

        # Retornar a resposta JSON com o usuário e o token
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token[1],  # Aqui está o valor do token
        })
    
# login 

class LoginApi(KnoxLoginView):
    permission_classes= (permissions.AllowAny, )
    def post(self, request, format = None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginApi, self).post(request, format=None)

            