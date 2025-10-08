from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    local = models.CharField(max_length=255)
    data = models.DateTimeField()
    imagem = models.ImageField(upload_to='eventos/', blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
