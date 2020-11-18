from rest_framework import serializers

from travel_anywhere.models import (Airport, City, Country, Hotel,
                                    Trip)


class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['destination_airport'] = AirportSerializer(instance.destination_airport).data
        response['departure_airport'] = AirportSerializer(instance.departure_airport).data
        response['destination_hotel'] = HotelSerializer(instance.destination_hotel).data
        return response


class AirportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airport
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["city"] = CitySerializer(instance.city).data
        return response


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["city"] = CitySerializer(instance.city).data
        return response


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ["id", "name", "country"]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["country"] = CountrySerializer(instance.country).data
        return response


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["continent"] = instance.continent.name
        return response





