from django.db import models
from django.urls import reverse
from datetime import date

SESSION = (
  ('M', 'Morning'),
  ('A', 'Afternoon'),
  ('E', 'Evening'),
)
# Create your models here.
class Insect(models.Model):
  name = models.CharField(max_length=100)
  color = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('insects_detail', kwargs={'pk': self.id})

class Plant(models.Model):
    name = models.CharField(max_length=100)
    genus = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    age = models.IntegerField()

    insects = models.ManyToManyField(Insect)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
      return reverse('detail', kwargs={'plant_id': self.id})

class Watering(models.Model):
  date = models.DateField('Watering date')
  session = models.CharField(
    max_length=1,
    choices=SESSION,
    default=SESSION[0][0]
  )

  plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_session_display()} on {self.date}"

  class Meta:
    ordering = ['-date']