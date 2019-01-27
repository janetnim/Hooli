from django.db import models
from .apps/authentication/models import User
from .apps/transportation/models import Car


class Location(models.Model):
  driver = models.OneToOneField(User)
  car = models.OneToOneField(Car)
  to = models.CharField(max_length=100, unique=True, db_index=True)
  from = models.CharField(max_length=100, unique=True, db_index=True)
  distance = models.IntegerField(max_length=1000)
  time_from = models.DateTimeField(auto_now=True)
  time_to = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.to
