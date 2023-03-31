from django.contrib import admin

from .models import Marca, Categoria, Veículo, Core, Acessório

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Veículo)
admin.site.register(Core)
admin.site.register(Acessório)