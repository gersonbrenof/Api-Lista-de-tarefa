from django.db import models

class Listas(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    discricao = models.TextField()
    data_inicio = models.DateTimeField(auto_now_add=True)
    data_fim = models.DateField(null = True, blank = True)
    finalizado = models.BooleanField(default=False)