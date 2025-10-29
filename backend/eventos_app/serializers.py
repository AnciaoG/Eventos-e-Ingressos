from rest_framework import serializers
from .models import Evento, Ingresso

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class IngressoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingresso
        fields = '__all__'

#É o tradutor entre o Django (que fala “modelo Python”) e o frontend (que fala “JSON”)