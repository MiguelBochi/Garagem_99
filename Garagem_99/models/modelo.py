from django.db import models
from Garagem_99.models import Marca, Categoria


class Modelo(models.Model):
    nome = models.CharField(
        max_length=50,
    )
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
