from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from Garagem_99.models import Modelo
from Garagem_99.serializers import ModeloSerializer


class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
