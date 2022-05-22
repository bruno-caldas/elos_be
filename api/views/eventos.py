from rest_framework import viewsets, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from eventos.models import Evento
from api.serializers import EventoSerializer

class EventosViewSet(viewsets.ModelViewSet):
    """Listando todos os eventos"""
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome_evento','data_evento']
    search_fields = ['nome_evento']
    # authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
