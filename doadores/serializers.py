from rest_framework import serializers
from doadores.models import Doadores

class DoadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doadores
<<<<<<< HEAD
        fields = '__all__'
        
=======
        fields = 'nome', 'sobrenome'
>>>>>>> 18f5c8a (Criação login de usuarios, api cadastro de doadores e doação)
