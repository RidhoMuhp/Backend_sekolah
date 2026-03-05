from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FasilitasViewSet

router = DefaultRouter()
router.register(r'fasilitas', FasilitasViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
