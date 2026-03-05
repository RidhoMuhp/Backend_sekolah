from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("judul", "isi", "gambar", "tanggal")
    search_fields = ("judul", "isi", "gambar", "tanggal")

