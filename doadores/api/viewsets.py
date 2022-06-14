from rest_framework import viewsets
from doadores.api import serializers
from doadores import models

class DoadoresViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DoadoresSerializer
    queryset = models.Doadores.objects.all()

class DoacaoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DoacaoSerializer
    queryset = models.Doacao.objects.all()