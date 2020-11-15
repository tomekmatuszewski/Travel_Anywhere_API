from django.urls import include, path
from rest_framework.routers import DefaultRouter

from travel_anywhere.api import api_views

router = DefaultRouter()
router.register(r"countries", api_views.CountryViewSet)
router.register(r"cities", api_views.CityViewSet)
router.register(r"airports", api_views.AirportsViewSet)
router.register(r"hotels", api_views.HotelViewSet)
router.register(r"trips", api_views.TripViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
