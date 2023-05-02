from django.contrib import admin

from .models import Marca, Categoria, Veículo, Cor, Acessório

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Veículo)
admin.site.register(Cor)
admin.site.register(Acessório)