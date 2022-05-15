from rest_framework import serializers

from parceiros.models import Parceiros

class ParceiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parceiros
        fields = '__all__'
