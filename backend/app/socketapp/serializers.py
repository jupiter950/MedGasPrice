from rest_framework import serializers
from .models import GasData

class GasSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasData
        fields = '__all__'