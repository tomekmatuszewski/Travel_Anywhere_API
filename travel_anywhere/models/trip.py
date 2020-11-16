from django.db import models

from travel_anywhere.models.airport import Airport
from travel_anywhere.models.hotel import Hotel


class Trip(models.Model):
    class Type(models.TextChoices):
        bed_and_breakfast = "BB"
        half_board = "HB"
        full_board = "FB"
        all_inclusive = "AI"

    type = models.CharField(choices=Type.choices, max_length=2)
    days_number = models.PositiveSmallIntegerField()
    departure_date = models.DateTimeField()
    return_date = models.DateTimeField()
    price_adults = models.FloatField()
    price_kids = models.FloatField()
    is_promoted = models.BooleanField(default=False)
    places_for_adults = models.PositiveSmallIntegerField()
    places_for_kids = models.PositiveSmallIntegerField()

    departure_airport = models.ForeignKey(
        Airport, on_delete=models.SET_NULL, null=True, related_name="trips_departure"
    )
    destination_airport = models.ForeignKey(
        Airport,
        on_delete=models.SET_NULL,
        null=True,
        related_name="trips_destination",
    )
    destination_hotel = models.ForeignKey(
        Hotel, on_delete=models.SET_NULL, null=True, related_name="trips"
    )

    def __str__(self):
        return f"Trip to {self.destination_hotel.name}"


