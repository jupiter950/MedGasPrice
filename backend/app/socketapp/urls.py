from django.urls import path
from . import views

urlpatterns = [
    path('', views.GasModelListAPIView.as_view(), name='gasmodel-list')
]