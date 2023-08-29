from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from Garagem_99.models import Veiculo
from Garagem_99.serializers import (VeiculoSerializer)


class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return VeiculoListSerializer
        elif self.action == "retrieve":
            return VeiculoDetailSerializer
        return VeiculoSerializer
