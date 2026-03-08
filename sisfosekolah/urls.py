from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/profil/", include("profil.urls")),
    path("api/fasilitas/", include("fasilitas.urls")),
    path("api/news/", include("news.urls")),
    path("api/galeri/", include("galeri.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)