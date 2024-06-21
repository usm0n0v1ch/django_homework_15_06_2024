from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True,upload_to='images')
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True,upload_to='images')
    bio = models.TextField(max_length=250)
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.name