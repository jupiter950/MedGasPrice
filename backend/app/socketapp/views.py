from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import GasData
from .serializers import GasSerializer

# Create your views here.
class GasModelListAPIView(generics.ListAPIView):
    queryset = GasData.objects.all()
    serializer_class = GasSerializer
