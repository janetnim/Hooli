from django.db import models
from .apps/authentication/models import User

class Car(models.Model):
  driver = models.OneToOneField(User)
  car_model = models.CharField(max_length=100)
  license_plate = models.CharField(max_length=100)
  current_location = models.CharField(max_length=100)

  def __str__(self):
    return self.license_plate