from django.db import models


class Continent(models.Model):
    class Name(models.TextChoices):
        europe = "Europe"
        north_am = "North America"
        south_am = "South America"
        asia = "Asia"
        aus_oceania = "Australia & Oceania"
        africa = "Africa"

    name = models.CharField(choices=Name.choices, max_length=32, unique=True)

    def __str__(self):
        return f"{self.name}"
