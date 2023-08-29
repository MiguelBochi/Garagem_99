from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from Garagem_99.models import Acessorio
from Garagem_99.serializers import (AcessorioSerializer)

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer
