from rest_framework import viewsets
from .models import Galeri
from .serializers import GaleriSerializer

class GaleriViewSet(viewsets.ModelViewSet):
    queryset = Galeri.objects.all().order_by('-id')[:6]
    serializer_class = GaleriSerializer
