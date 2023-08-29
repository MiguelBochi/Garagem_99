from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from usuario.router import router as usuario_router


from Garagem_99.views import (AcessorioViewSet, CategoriaViewSet, CorViewSet,
                              MarcaViewSet, VeiculoViewSet)
from uploader.router import router as uploader_router


router = DefaultRouter()
router.register("Acessorios", AcessorioViewSet)
router.register("Categorias", CategoriaViewSet)
router.register("Cores", CorViewSet)
router.register("Marcas", MarcaViewSet)
router.register("Veiculos", VeiculoViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/", include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
