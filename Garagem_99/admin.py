from django.contrib import admin

from .models import Marca, Categoria

admin.site.register(Categoria)
admin.site.register(Marca)