from rest_framework import viewsets
from doadores.api import serializers
from doadores import models

class DoadoresViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DoadoresSerializer
    queryset = models.Doadores.objects.all()
<<<<<<< HEAD
=======

class DoacaoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DoacaoSerializer
    queryset = models.Doacao.objects.all()
>>>>>>> 18f5c8a (Criação login de usuarios, api cadastro de doadores e doação)
