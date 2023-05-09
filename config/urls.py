from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from Garagem_99.views import 


router = DefaultRouter()
router.register("Marcas", MarcaViewSet)
router.register("Veiculo", VeiculoViewSet)
router.register("Categoria", CategoriaViewSet)
router.register("Cores", CorViewSet)
router.register("Acessorio", AcessorioViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
