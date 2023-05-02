from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from Garagem_99.views import MarcaViewSet
from Garagem_99.views import VeiculoViewSet
from Garagem_99.views import CategoriaViewSet
from Garagem_99.views import CorViewSet
from Garagem_99.views import AcessórioViewSet

router = DefaultRouter()
router.register("Marcas", MarcaViewSet)
router.register("Veiculo", VeiculoViewSet)
router.register("Categoria", CategoriaViewSet)
router.register("Cores", CorViewSet)
router.register("Acessório", AcessórioViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
