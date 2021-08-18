from django.db import models

# Create your models here.
class Mouvement(models.Models):
    location = models.CharField(max_lenght=200)
    destination=models.CharField(max_lenght=200)
    distance= models.DecimalField(max_digits=ID, decimal_places=2)
    created=models.DataTimeField()

    def __str__(self):
        return "Distance from {self.location} to {self.destination} is {self.distance} la"