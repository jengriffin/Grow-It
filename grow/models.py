from django.db import models

# Create your models here.


class Plant(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()
    info = models.TextField()

    def __str__(self):
        return self.name


class Blog(models.Model):
    plants = models.ForeignKey(
        Plant, on_delete=models.CASCADE, related_name='plants')
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title


class User(models.Model):
    email = models.EmailField(max_length=200)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
