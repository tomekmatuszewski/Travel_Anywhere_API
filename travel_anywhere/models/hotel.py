from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from travel_anywhere.models.city import City


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    standard = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    description = models.TextField(blank=True, null=True, max_length=250)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="hotels")

    def __str__(self):
        return f"{self.name}"
