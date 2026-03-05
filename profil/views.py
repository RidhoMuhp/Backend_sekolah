from django.shortcuts import render
from rest_framework import viewsets
from .models import ProfilSekolah
from .serializers import ProfilSekolahSerializer

class ProfilSekolahViewSet(viewsets.ModelViewSet):
    queryset = ProfilSekolah.objects.all()
    serializer_class = ProfilSekolahSerializer


