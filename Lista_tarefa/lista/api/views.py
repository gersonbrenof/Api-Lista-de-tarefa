from rest_framework import generics, permissions
from lista.models import Listas
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, generics
from lista.api.serializers import ListaSerializer
from datetime import date
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
class ListaViewSet(ModelViewSet):
    serializer_class = ListaSerializer
    queryset = Listas.objects.all()
    # permission_classes = [AllowAny]

    # @action(detail=True, methods=['post', 'get'])
    # def finalizar_tarefa(self, request , pk=None):
    #     lista = self.get_object()

    #     lista.finalizado = True
    #     lista.data_fim = date.today()
    #     lista.save()

    #     Serializer = self.get_serializer(lista)
    #     return Response(Serializer.data)
@method_decorator(csrf_exempt, name='dispatch')
class ListaAPIView(generics.ListCreateAPIView):
    serializer_class = ListaSerializer
    queryset = Listas.objects.all()