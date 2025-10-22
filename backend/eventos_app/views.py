from rest_framework import generics
from .models import Evento, Ingresso
from .serializers import EventoSerializer, IngressoSerializer

# Listar todos os eventos
class EventoListView(generics.ListAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

# Detalhe de um evento
class EventoDetailView(generics.RetrieveAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

# Criar ingresso (simulando compra)
class IngressoCreateView(generics.CreateAPIView):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer
