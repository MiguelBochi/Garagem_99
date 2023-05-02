from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from Garagem_99.views import MarcaViewSet

router = DefaultRouter()
router.register(r"Marcas", MarcaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
