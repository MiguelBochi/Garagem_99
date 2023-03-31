from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50,)
    nacionalidade = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nome.upper()


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
class Acessório(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Core(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
class Veículo(models.Model):
    ano = models.IntegerField(default=0, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    cor = models.ForeignKey(Core, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.preco} ,{self.ano}, {self.cor}, {self.modelo}, {self.categoria}"
    