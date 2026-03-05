from django.db import models

class ProfilSekolah(models.Model):
    nama_sekolah = models.CharField(max_length=200)
    deskripsi = models.TextField()
    alamat = models.TextField()
    telepon = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    logo = models.ImageField(upload_to="logo/", blank=True, null=True)

    def __str__(self):
        return self.nama_sekolah
