from rest_framework import serializers
from .models import ProfilSekolah

class ProfilSekolahSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilSekolah
        fields = '__all__'
