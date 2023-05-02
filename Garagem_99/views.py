from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from Garagem_99.models import Marca
from Garagem_99.serializers import MarcaSerializer
from Garagem_99.models import Veículo
from Garagem_99.serializers import VeiculoSerializer
from Garagem_99.models import Cor
from Garagem_99.serializers import CorSerializer
from Garagem_99.models import Categoria
from Garagem_99.serializers import CategoriaSerializer
from Garagem_99.models import Acessório
from Garagem_99.serializers import AcessorioSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
class VeiculoViewSet(ModelViewSet):
    queryset = Veículo.objects.all()
    serializer_class = VeiculoSerializer
class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer
class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
class AcessórioViewSet(ModelViewSet):
    queryset = Acessório.objects.all()
    serializer_class = AcessorioSerializer

