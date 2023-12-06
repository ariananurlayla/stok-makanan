from django.db import models
from django.contrib.auth.models import User  # import model


class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # menghubungkan produk dengan satu user (many to one relationship), dimana setiap produk pasti terasosiasikan dengan seorang user
    # lakukan migrasi model jika terjadi perubahan pada model
