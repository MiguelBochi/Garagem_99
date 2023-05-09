from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from Garagem_99.models import Acessorio, Categoria, Cor, Marca , Veiculo
from Garagem_99.serializers import AcessorioSerializer, MarcaSerializer, CategoriaSerializer, CorSerializer , VeiculoSerializer, VeiculoListSerializer, VeiculoDetailSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return VeiculoListSerializer
        elif self.action == "retrieve":
            return VeiculoDetailSerializer
        return VeiculoSerializer
class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer
class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer


