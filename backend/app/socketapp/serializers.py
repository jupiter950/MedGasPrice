from rest_framework import serializers
from .models import GasData, MedGasPrice

class GasSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasData
        fields = '__all__'

class MedGasPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedGasPrice
        fields = '__all__'