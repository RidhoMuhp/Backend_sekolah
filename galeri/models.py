from django.db import models

class Galeri(models.Model):
    JENIS_CHOICES = (
        ('foto', 'Foto'),
        ('video', 'Video'),
    )

    judul = models.CharField(max_length=255)
    file = models.FileField(upload_to="galeri/")  # bisa foto/video
    jenis = models.CharField(max_length=10, choices=JENIS_CHOICES, default='foto')
    deskripsi = models.TextField(blank=True, null=True)
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul
