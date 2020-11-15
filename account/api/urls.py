from django.urls import path

from account.api import api_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("api/register", api_views.RegisterUser.as_view(), name="register"),
    path("api/login", obtain_auth_token, name="login"),
]
