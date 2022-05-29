from rest_framework import viewsets, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from parceiros.models import Parceiros
from api.serializers import ParceiroSerializer

class ParceirosViewSet(viewsets.ModelViewSet):
    """Listando todos os parceiros"""
    permission_classes = (IsAuthenticated)
    queryset = Parceiros.objects.all()
    serializer_class = ParceiroSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome_parceiro']
    search_fields = ['nome_parceiro']
<<<<<<< HEAD
    authentication_classes = [BasicAuthentication]
    
=======
    # authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
>>>>>>> c380b57 (forcing athenticated frontend)
