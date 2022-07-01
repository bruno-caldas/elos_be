from rest_framework import serializers
from doadores import models

class DoadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doadores
        fields = '__all__'
        fields = 'nome', 'sobrenome', 'dt_nasc', 'endereco', 'numero', 'complemento', 'celular', 'Intencao', 'Doador' 

class DoacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doacao
        fields = 'Classificacao', 'Descricao', 'Estado', 'Quantidade', 'Doador'
            