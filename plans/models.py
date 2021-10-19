from django.db import models

# Create your models here.
class Destination(models.Model):
  destination = models.CharField(max_length=255)
  image = models.URLField(max_length=255)

  def __str__(self):
      return self.destination

class Plan(models.Model):
  id_destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
  destination_name = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  url_img = models.URLField(max_length=255, blank=False)

  def __str__(self):
      return self.destination_name