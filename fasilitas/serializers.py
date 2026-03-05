from rest_framework import serializers
from .models import Fasilitas

class FasilitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fasilitas
        fields = '__all__'
