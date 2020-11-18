from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from account.api import api_views

router = DefaultRouter()
router.register(r"all_users", api_views.UsersViewSet)

urlpatterns = [
    path("api/register", api_views.RegisterUser.as_view(), name="register"),
    path("api/login", obtain_auth_token, name="login"),
    path("api/user-profile", api_views.UserProfileView.as_view(), name="user-profile"),
    path("api/", include(router.urls)),
]
