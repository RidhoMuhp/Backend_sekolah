from django.contrib import admin
from .models import ProfilSekolah

@admin.register(ProfilSekolah)
class ProfilSekolahAdmin(admin.ModelAdmin):
    list_display = ("nama_sekolah", "deskripsi", "alamat", "email", "telepon", "logo")
    search_fields = ("nama_sekolah", "deskripsi", "alamat", "email", "telepon", "logo")

