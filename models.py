from django.db import models
#creer un model
class Mouvement(models.Model):
    location = models.CharField(max_lenght=200)
    destination=models.CharField(max_lenght=200)
    distance= models.DecimalField(max_digits=10, decimal_places=2)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Distance from {self.location} to {self.destination} is {self.distance} km"