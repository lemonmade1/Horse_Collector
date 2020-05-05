from django.db import models
from django.urls import reverse

# A tuple of 2-tuples
MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

# Create your models here.
class Horse(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('horses_detail', kwargs={'pk': self.id})

class Feeding(models.Model):
  date = models.DateField()
  meal = models.CharField(
    max_length=1,

    # add the 'choices' field option
    choices=MEALS,

    # set the default value for meal to be 'B'
    default=MEALS[0][0],
  )

  horse = models.ForeignKey(Horse, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"  