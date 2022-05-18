from rest_framework import viewsets, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from parceiros.models import Parceiros
from api.serializers import ParceiroSerializer

class ParceirosViewSet(viewsets.ModelViewSet):
    """Listando todos os parceiros"""
    queryset = Parceiros.objects.all()
    serializer_class = ParceiroSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome_parceiro']
    search_fields = ['nome_parceiro']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
