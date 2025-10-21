from django.test import TestCase
from apps.eventos.models import Evento
from django.utils import timezone

class TestEventos(TestCase):
    def setUp(self):
        self.evento = Evento.objects.create(
            nome='Show Teste QA',
            descricao='Evento criado para testes automatizados',
            local='Teatro Central',
            data=timezone.now()
        )

    def test_criar_evento(self):
        evento = Evento.objects.get(nome='Show Teste QA')
        self.assertEqual(evento.descricao, 'Evento criado para testes automatizados')
        self.assertEqual(evento.local, 'Teatro Central')

    def test_listar_eventos(self):
        eventos = Evento.objects.all()
        self.assertEqual(eventos.count(), 1)
        self.assertEqual(str(eventos[0]), 'Show Teste QA')
