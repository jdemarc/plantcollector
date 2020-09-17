from django.db import models
from django.urls import reverse

MAINTENANCE = (
  ('C', 'Corrective'),
  ('P', 'Preventative'),
  ('R', 'Routine'),
)
# Create your models here.
class Toy(models.Model):
    name = models.CharField(max_length=100)
    maker = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    release_year = models.IntegerField()
    value = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
      return reverse('detail', kwargs={'toy_id': self.id})

class Maintaining(models.Model):
  date = models.DateField('Maintenance date')
  care = models.CharField(
    max_length=1,
    choices=MAINTENANCE,
    default=MAINTENANCE[0][0]
  )

  toy = models.ForeignKey(Toy, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_care_display()} on {self.date}"

'''
toys = [
  Toy('Attack Armor Batman', 'Mattel', 'Batman superhero action figure', 2004, 400),
  Toy('Scratch the Cat', 'Playmates', 'TMNT minor character Scratch', 1993, 1500),
  Toy('Green Beret G.I. Joe', 'Hasbro', 'American hero toy G.I. Joe', 1966, 2100)
]
'''