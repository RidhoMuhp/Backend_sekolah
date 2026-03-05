from django.shortcuts import render
from rest_framework import viewsets
from .models import Fasilitas
from .serializers import FasilitasSerializer

class FasilitasViewSet(viewsets.ModelViewSet):
    queryset = Fasilitas.objects.all()
    serializer_class = FasilitasSerializer

