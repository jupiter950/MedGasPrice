from django.urls import path
from . import views

urlpatterns = [
    path('gasprices', views.GasModelListAPIView.as_view(), name='gasmodel-list'),
    path('medprice', views.MedGasModelListAPIView.as_view(), name='medmodel-list'),
]