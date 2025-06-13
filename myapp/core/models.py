from django.db import models

# Create your models here.


from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=100)
    revolution_time = models.FloatField()
    rotation_time = models.FloatField()
    radius = models.FloatField()
    average_temp = models.FloatField()

    def __str__(self):
        return self.name

