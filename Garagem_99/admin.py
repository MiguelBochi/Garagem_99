from django.contrib import admin

from .models import Acessorio, Categoria, Cor, Marca, Modelo, Veiculo

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Veiculo)
admin.site.register(Cor)
admin.site.register(Acessorio)