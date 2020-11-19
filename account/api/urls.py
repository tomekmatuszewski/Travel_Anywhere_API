from django.urls import include, path
from rest_framework.routers import DefaultRouter

from account.api import api_views

router = DefaultRouter()
router.register(r"all-users", api_views.UsersViewSet)

urlpatterns = [
    path("api/register", api_views.RegisterUser.as_view(), name="register"),
    path("api/login", api_views.ObtainTokenView.as_view(), name="login"),
    path("api/user-profile", api_views.UserProfileView.as_view(), name="user-profile"),
    path("api/change-password", api_views.ChangePasswordView.as_view(), name="change-password"),
    path("api/", include(router.urls)),
]
