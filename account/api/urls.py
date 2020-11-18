from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from account.api import api_views

router = DefaultRouter()
router.register(r"all_users", api_views.UsersViewSet)

urlpatterns = [
    path("api/register", api_views.RegisterUser.as_view(), name="register"),
    path("api/login", obtain_auth_token, name="login"),
    path("api/", include(router.urls)),
]
