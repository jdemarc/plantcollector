from django.db import models

# Create your models here.
class Toy(models.Model):
    name = models.CharField(max_length=100)
    maker = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    release_year = models.IntegerField()
    value = models.IntegerField()

    def __str__(self):
        return self.name
