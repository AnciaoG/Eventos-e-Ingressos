from django.urls import path
from .views import EventoListView, EventoDetailView, IngressoCreateView

urlpatterns = [
    path('eventos/', EventoListView.as_view(), name='evento-list'),
    path('eventos/<int:pk>/', EventoDetailView.as_view(), name='evento-detail'),
    path('ingressos/', IngressoCreateView.as_view(), name='ingresso-create'),
]
