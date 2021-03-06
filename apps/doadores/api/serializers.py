from rest_framework import serializers
from doadores import models

class DoadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doadores
        fields = 'nome', 'sobrenome', 'dt_nasc', 'cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'celular', 'Intencao', 'username' 


class DoacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doacao
        fields = 'classificacao', 'descricao', 'estado', 'quantidade', 'username'
    
        
        
        