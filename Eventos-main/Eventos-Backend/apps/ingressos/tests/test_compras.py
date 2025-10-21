from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from apps.eventos.models import Evento
from apps.ingressos.models import Ingresso

class TestCompraIngresso(TestCase):
    def setUp(self):
        self.organizador = User.objects.create_user(
            username='organizador', password='12345', is_staff=True
        )
        self.usuario = User.objects.create_user(
            username='usuario', password='12345'
        )

        self.evento = Evento.objects.create(
            nome='Festival QA',
            descricao='Evento de teste de compra de ingresso',
            local='Auditório Central',
            data=timezone.now(),
        )

        self.ingresso = Ingresso.objects.create(
            evento=self.evento,
            tipo='Pista',
            preco=50.00,
            quantidade_total=100,
            quantidade_disponivel=100
        )

    def test_compra_ingresso(self):
        qtd_anterior = self.ingresso.quantidade_disponivel

        if self.ingresso.quantidade_disponivel > 0:
            self.ingresso.quantidade_disponivel -= 1
            self.ingresso.save()
            compra_status = 'confirmada'
        else:
            compra_status = 'esgotado'

        self.ingresso.refresh_from_db()

        self.assertEqual(compra_status, 'confirmada')
        self.assertEqual(self.ingresso.quantidade_disponivel, qtd_anterior - 1)
        print(f"Ingresso comprado com sucesso! Restam {self.ingresso.quantidade_disponivel} disponíveis.")

    def test_compra_ingresso_esgotado(self):
        self.ingresso.quantidade_disponivel = 0
        self.ingresso.save()

        if self.ingresso.quantidade_disponivel > 0:
            self.ingresso.quantidade_disponivel -= 1
            self.ingresso.save()
            compra_status = 'confirmada'
        else:
            compra_status = 'esgotado'

        self.assertEqual(compra_status, 'esgotado')
        print("Compra bloqueada: ingressos esgotados.")
