from rest_framework import serializers
from lista.models import Listas
from datetime import date
class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listas
        fields = "__all__"
    def update(self, instance, validated_data):
        instance.finalizado = validated_data.get('finalizado', instance.finalizado)
        if instance.finalizado:
            instance.data_fim = date.today()
            instance.save()

            return instance