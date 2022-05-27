from rest_framework import serializers
from doadores import models

class DoadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doadores
        fields = '__all__'
        