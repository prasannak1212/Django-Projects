from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100)
    food = models.CharField(max_length=100)
    habitat = models.CharField(max_length=500)
    documentary_title = models.CharField(max_length=500)
    details = models.TextField()
    image = models.ImageField(upload_to='animal_images/')

    def __str__(self):
        return self.name
