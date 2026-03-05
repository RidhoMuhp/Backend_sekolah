from django.db import models

class News(models.Model):
    judul = models.CharField(max_length=255)
    isi = models.TextField()
    gambar = models.ImageField(upload_to="news/", blank=True, null=True)
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul
