from django.db import models

class Mission(models.Model):
    location = models.CharField(max_length=180)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.location