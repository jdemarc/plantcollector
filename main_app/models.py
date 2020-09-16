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

'''
toys = [
  Toy('Attack Armor Batman', 'Mattel', 'Batman superhero action figure', 2004, 400),
  Toy('Scratch the Cat', 'Playmates', 'TMNT minor character Scratch', 1993, 1500),
  Toy('Green Beret G.I. Joe', 'Hasbro', 'American hero toy G.I. Joe', 1966, 2100)
]
'''