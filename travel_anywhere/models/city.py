from django.db import models

from travel_anywhere.models.country import Country


class City(models.Model):
    name = models.CharField(max_length=150)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="cities"
    )

    def __str__(self):
        return f"{self.name}"
