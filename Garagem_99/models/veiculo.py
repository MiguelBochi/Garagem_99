from django.db import models
from Garagem_99.models import Cor, Acessorio, Modelo
from uploader.models import Image


class Veiculo(models.Model):
    ano = models.IntegerField(default=0, null=True)
    descricao = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE)
    acessorio = models.ManyToManyField(Acessorio, related_name="+",)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    capa = models.ManyToManyField(
        Image,
        related_name="+",
    )

    def __str__(self):
        return f"{self.modelo} {self.cor} {self.ano} {self.preco}"

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"
