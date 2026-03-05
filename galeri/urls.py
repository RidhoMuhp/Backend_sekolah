from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GaleriViewSet

router = DefaultRouter()
router.register(r'galeri', GaleriViewSet)

urlpatterns = router.urls
