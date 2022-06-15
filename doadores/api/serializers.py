from rest_framework import serializers
from doadores import models

class DoadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doadores
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = 'nome', 'sobrenome', 'dt_nasc', 'endereco', 'numero', 'complemento', 'celular', 'Intenção', 'Doador' 


class DoacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doacao
        fields = 'Classificacao', 'Descricao', 'Estado', 'Quantidade', 'Doador'
    
        
>>>>>>> 18f5c8a (Criação login de usuarios, api cadastro de doadores e doação)
        