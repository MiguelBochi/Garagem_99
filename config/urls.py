from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from usuario.router import router as usuario_router


from Garagem_99.views import (
    AcessorioViewSet,
    CategoriaViewSet,
    CorViewSet,
    MarcaViewSet,
    VeiculoViewSet,
)
from uploader.router import router as uploader_router
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

router = DefaultRouter()
router.register("acessorios", AcessorioViewSet)
router.register("categorias", CategoriaViewSet)
router.register("cores", CorViewSet)
router.register("marcas", MarcaViewSet)
router.register("veiculos", VeiculoViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/", include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
