from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import GasData, MedGasPrice
from .serializers import GasSerializer, MedGasPriceSerializer

# Create your views here.
class GasModelListAPIView(generics.ListAPIView):
    queryset = GasData.objects.all()
    serializer_class = GasSerializer
class MedGasModelListAPIView(generics.ListAPIView):
    queryset = MedGasPrice.objects.all()
    serializer_class = MedGasPriceSerializer
