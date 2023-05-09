from rest_framework.serializers import ModelSerializer

from Garagem_99.models import Acessorio, Categoria, Cor, Marca , Veiculo

class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"
class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
class CorSerializer(ModelSerializer):
    class Meta:
        model = Cor
        fields = "__all__"
class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"
class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"
class VeiculoListSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ["id", "cor", "preco","ano", "modelo",]      
class VeiculoDatailSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ["id", "preco"]
        depth = 1


