from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateField()
    horario = models.TimeField()
    local = models.CharField(max_length=200)
    imagem = models.URLField(blank=True, null=True)
    ingressos_disponiveis = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome

class Ingresso(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='ingressos')
    quantidade = models.PositiveIntegerField(default=1)
    comprador_nome = models.CharField(max_length=100, blank=True, null=True)
    qr_code = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.quantidade} ingresso(s) - {self.evento.nome}'
