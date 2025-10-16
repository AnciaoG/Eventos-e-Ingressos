from django.db import models
from apps.eventos.models import Evento

class Ingresso(models.Model):
    evento = models.ForeignKey(Evento, related_name='ingressos', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100, default='Padrão')
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade_total = models.PositiveIntegerField()
    quantidade_disponivel = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.tipo} - {self.evento.nome}"
