from django.urls import path

from account.api import api_views

urlpatterns = [
    path("api/register", api_views.RegisterUser.as_view(), name="register"),
]
