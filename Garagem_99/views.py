from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from Garagem_99.models import Marca
from Garagem_99.serializers import MarcaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
