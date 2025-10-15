from django.shortcuts import render
from rest_framework import viewsets
from .models import Ingresso
from .serializers import IngressoSerializer

class IngressoViewSet(viewsets.ModelViewSet):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer

