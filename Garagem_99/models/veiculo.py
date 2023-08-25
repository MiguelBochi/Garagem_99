from django.db import models
from Garagem_99.models import Cor,Acessorio,Modelo

class Veiculo(models.Model):
    ano = models.IntegerField(default=0, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE)
    cessorio = models.ForeignKey(Acessorio, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.preco} ,{self.ano}, {self.cor}, {self.modelo}, {self.categoria}"

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"
