from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    enrollment = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    date = models.DateField(auto_created=True)

    def __str__(self):
        return self.name
