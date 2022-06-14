from rest_framework import serializers
from doadores.models import Doadores

class DoadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doadores
        fields = 'nome', 'sobrenome'