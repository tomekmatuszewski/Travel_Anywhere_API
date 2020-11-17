
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from travel_anywhere.api.serializers import (AirportSerializer, HotelSerializer, TripSerializer)
from travel_anywhere.models import (Airport, Hotel, Trip)


class TripViewSet(viewsets.ModelViewSet):

    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["type", "destination_hotel__name", "destination_airport__name"]


class TripHotelView(generics.GenericAPIView):

    serializer_class = HotelSerializer

    def get(self, request, *args, **kwargs):
        id_ = self.kwargs['pk']
        queryset = Trip.objects.get(pk=id_).destination_hotel
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)


class TripAirportView(generics.GenericAPIView):

    serializer_class = AirportSerializer

    def get(self, request, *args, **kwargs):
        id_ = self.kwargs['pk']
        queryset = Trip.objects.get(pk=id_)
        if self.kwargs['slug'] == "airport-dest":
            queryset = queryset.destination_airport
        elif self.kwargs['slug'] == "airport-dep":
            queryset = queryset.departure_airport
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)


class AirportsViewSet(viewsets.ModelViewSet):

    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    filter_backends = [SearchFilter, OrderingFilter]


class HotelViewSet(viewsets.ModelViewSet):

    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "standard", "city__name"]
