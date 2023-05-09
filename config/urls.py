from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from Garagem_99.views import (AcessorioViewSet, CategoriaViewSet, CorViewSet,
                              MarcaViewSet, VeiculoViewSet)

router = DefaultRouter()
router.register("Acessorios", AcessorioViewSet)
router.register("Categorias", CategoriaViewSet)
router.register("Cores", CorViewSet)
router.register("Marcas", MarcaViewSet)
router.register("Veiculos", VeiculoViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
