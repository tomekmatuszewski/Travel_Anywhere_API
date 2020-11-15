from rest_framework import viewsets

from travel_anywhere.api.serializers import (AirportSerializer, CitySerializer,
                                             ContinentSerializer,
                                             CountrySerializer,
                                             HotelSerializer, TripSerializer)
from travel_anywhere.models import (Airport, City, Continent, Country, Hotel,
                                    Trip)


class ContinentViewSet(viewsets.ModelViewSet):

    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer


class CountryViewSet(viewsets.ModelViewSet):

    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityViewSet(viewsets.ModelViewSet):

    queryset = City.objects.all()
    serializer_class = CitySerializer


class AirportsViewSet(viewsets.ModelViewSet):

    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class HotelViewSet(viewsets.ModelViewSet):

    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class TripViewSet(viewsets.ModelViewSet):

    permission_classes = []

    queryset = Trip.objects.all()
    serializer_class = TripSerializer
