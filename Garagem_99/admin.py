from django.contrib import admin

from .models import Marca, Categoria, Veiculo, Cor, Acessorio

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Cor)
admin.site.register(Acessorio)