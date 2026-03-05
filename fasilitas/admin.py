from django.contrib import admin
from .models import Fasilitas

@admin.register(Fasilitas)
class FasilitasAdmin(admin.ModelAdmin):
    list_display = ("nama", "deskripsi", "icon", "gambar")
    search_fields = ("nama", "deskripsi", "icon", "gambar")

