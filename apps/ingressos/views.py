from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Ingresso
from .serializers import IngressoSerializer

class IngressoViewSet(viewsets.ModelViewSet):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer

    @action(detail=True, methods=['post'])
    def comprar(self, request, pk=None):
        ingresso = self.get_object()

        if ingresso.quantidade_disponivel > 0:
            ingresso.quantidade_disponivel -= 1
            ingresso.save()
            return Response(
                {"mensagem": "Compra confirmada!", "restantes": ingresso.quantidade_disponivel},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"erro": "Ingressos esgotados!"},
                status=status.HTTP_400_BAD_REQUEST
            )
