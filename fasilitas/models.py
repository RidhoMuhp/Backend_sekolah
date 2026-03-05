from django.db import models

class Fasilitas(models.Model):
    nama = models.CharField(max_length=200)
    deskripsi = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=100, help_text="Nama icon lucide/react atau fontawesome")
    gambar = models.ImageField(upload_to="fasilitas/", blank=True, null=True)

    def __str__(self):
        return self.nama


