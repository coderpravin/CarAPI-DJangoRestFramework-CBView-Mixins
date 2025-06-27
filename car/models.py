from django.db import models

# Create your models here.
color_car = [
    ("Blue", "Blue"),
    ("Black", "Black"),
    ("Green", "Green"),
    ("Orange", "Orange"),
    ("Red", "Red"),
    ("Yellow", "Yellow"),
] 

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=50, choices=color_car)

    def __str__(self):
        return self.name
