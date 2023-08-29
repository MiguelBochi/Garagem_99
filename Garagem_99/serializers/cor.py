from rest_framework.serializers import ModelSerializer

from Garagem_99.models import Cor



class CorSerializer(ModelSerializer):
    class Meta:
        model = Cor
        fields = "__all__"