from django.db import models

# Create your models here.

from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=100)
    number_of_days = models.IntegerField(help_text="Number of days in a year")
    distance_from_sun = models.FloatField(help_text="Distance in million km")
    has_rings = models.BooleanField(default=False)

    def __str__(self):
        return self.name
