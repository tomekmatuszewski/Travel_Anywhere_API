from django.db import models

from travel_anywhere.models.continent import Continent


class Country(models.Model):
    name = models.CharField(max_length=50)
    continent = models.ForeignKey(
        Continent, on_delete=models.CASCADE, related_name="countries"
    )

    def __str__(self):
        return f"{self.name}"
