from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from Garagem_99.models import Cor
from Garagem_99.serializers import (CorSerializer)

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer

