from rest_framework import viewsets
from api.serializers import doadores
from doadores import models

class DoadoresViewSet(viewsets.ModelViewSet):
    serializer_class = doadores.DoadoresSerializer
    queryset = models.Doadores.objects.all()

class DoacaoViewSet(viewsets.ModelViewSet):
    serializer_class = doadores.DoacaoSerializer
    queryset = models.Doacao.objects.all()
