from rest_framework import serializers

from travel_anywhere.models import (Airport, City, Continent, Country, Hotel,
                                    Trip)


class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = "__all__"
        depth = 1


class AirportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airport
        fields = ["name", "city"]
        depth = 3


class HotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hotel
        fields = ["name", "standard", "description", "city"]
        depth = 3




