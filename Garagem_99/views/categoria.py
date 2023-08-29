from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from Garagem_99.models import Categoria
from Garagem_99.serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
