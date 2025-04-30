from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    kategori = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    lokasi = models.CharField(max_length=100)
    flag = models.CharField(max_length=100)

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.CharField(max_length=100)

class Task(models.Model):
    nama_task = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField() 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama_task  # Menampilkan nama task di admin atau shell Django

