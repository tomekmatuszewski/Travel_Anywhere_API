from django.urls import include, path
from rest_framework.routers import DefaultRouter

from travel_anywhere.api import api_views

router = DefaultRouter()
router.register(r"airports", api_views.AirportsViewSet)
router.register(r"hotels", api_views.HotelViewSet)
router.register(r"trips", api_views.TripViewSet)
router.register(r"cities", api_views.CityView)
router.register(r"countries", api_views.CountryView)

urlpatterns = [
    path('api/', include(router.urls)),
    path(
        "api/trips/<int:pk>/hotel", api_views.TripHotelView.as_view(), name="trip-hotel"
    ),
    path("api/trips/<int:pk>/<slug:slug>", api_views.TripAirportView.as_view()),
]
