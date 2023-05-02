from rest_framework.serializers import ModelSerializer

from Garagem_99.models import Marca
from Garagem_99.models import Cor
from Garagem_99.models import Veículo
from Garagem_99.models import Acessório
from Garagem_99.models import Categoria

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"
class CorSerializer(ModelSerializer):
    class Meta:
        model = Cor
        fields = "__all__"
class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veículo
        fields = "__all__"

class VeiculoMarcaSerializer(ModelSerializer):
    class Meta:
        model = Veículo
        fields = ["id", "titulo", "preco"]

class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = Acessório
        fields = "__all__"
class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
