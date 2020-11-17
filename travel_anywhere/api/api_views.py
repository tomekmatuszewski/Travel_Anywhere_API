from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

from travel_anywhere.api.serializers import (AirportSerializer, CitySerializer,
                                             CountrySerializer,
                                             HotelSerializer, TripSerializer)
from travel_anywhere.models import (Airport, City, Country, Hotel,
                                    Trip)


class CountryViewSet(viewsets.ModelViewSet):

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "continent__name"]


class CityViewSet(viewsets.ModelViewSet):

    queryset = City.objects.all()
    serializer_class = CitySerializer


class AirportsViewSet(viewsets.ModelViewSet):

    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    filter_backends = [SearchFilter, OrderingFilter]


class HotelViewSet(viewsets.ModelViewSet):

    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "standard", "city__name"]


class TripViewSet(viewsets.ModelViewSet):

    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["type", "destination_hotel__name"]



