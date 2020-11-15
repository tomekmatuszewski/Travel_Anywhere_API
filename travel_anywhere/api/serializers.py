from rest_framework import serializers

from travel_anywhere.models import (Airport, City, Continent, Country, Hotel,
                                    Trip)


class TripSerializer(serializers.ModelSerializer):

    country = serializers.CharField(source="destination_hotel.city.country.name", read_only=True)
    city = serializers.CharField(source="destination_hotel.city.name", read_only=True)
    airport_departure = serializers.CharField(source="departure_airport.name", read_only=True)
    airport_destination = serializers.CharField(source="destination_airport.name", read_only=True)
    hotel = serializers.CharField(source="destination_hotel.name", read_only=True)

    class Meta:
        model = Trip
        fields = ["id", "type", "days_number", "departure_date", "return_date",
                  "price_adults", "price_kids", "is_promoted",
                  "places_for_adults", "places_for_kids", "airport_departure",
                  "airport_destination", "hotel", "city", "country"]


class AirportSerializer(serializers.ModelSerializer):
    trips_departure = TripSerializer(many=True, read_only=True)
    trips_destination = TripSerializer(many=True, read_only=True)

    class Meta:
        model = Airport
        fields = ["name", "city", "trips_departure", "trips_destination"]


class HotelSerializer(serializers.ModelSerializer):

    trips = TripSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ["name", "standard", "description", "city", "trips"]


class CitySerializer(serializers.ModelSerializer):

    hotels = HotelSerializer(many=True, read_only=True)
    airports = AirportSerializer(many=True, read_only=True)
    country_name = serializers.CharField(source="country.name", read_only=True)

    class Meta:
        model = City
        fields = ["name", "country", "country_name", "hotels", "airports"]


class CountrySerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, read_only=True)
    continent_name = serializers.CharField(source="continent.name", read_only=True)

    class Meta:
        model = Country
        fields = ["id", "name", "continent", "continent_name", "cities"]


