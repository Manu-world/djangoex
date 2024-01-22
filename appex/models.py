from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    price = models.FloatField(default=0.00)


    def __str__(self):
        return self.title