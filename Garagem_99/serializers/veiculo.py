from rest_framework.serializers import ModelSerializer
from Garagem_99.models import Veiculo
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer


class VeiculoSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    Foto = ImageSerializer(required=False, read_only=True)


class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"


class VeiculoDetailSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = [
            "id",
            "cor",
            "preco",
            "ano",
            "modelo",
        ]
        capa = ImageSerializer(required=False)


class VeiculoListSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ["id", "preco"]
        depth = 1
