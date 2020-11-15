import pytest
from django.urls import reverse
from account.models import UserProfile


@pytest.mark.django_db
class TestRegisterUser:
    def test_register_user(self, client):
        response = client.post(
            reverse("register"),
            {
                "username": "test_user",
                "email": "test@gmail.com",
                "password": "test12345",
                "password2": "test12345",
            },
        )
        assert response.status_code == 201
        assert response.data == {
            "response": "User Created Successfully.  Now perform Login to get your token",
            "username": "test_user",
            "email": "test@gmail.com",
        }
        assert UserProfile.objects.first().user.username == "test_user"

    def test_register_user_failed(self, client):
        response = client.post(
            reverse("register"),
            {
                "username": "",
                "email": "test@gmail.com",
                "password": "test12345",
                "password2": "test12345",
            },
        )
        assert response.status_code == 400
        assert response.data == {"username": ["This field may not be blank."]}

    def test_register_user_failed_wrong_password_confirmation(self, client):
        response = client.post(
            reverse("register"),
            {
                "username": "testuser",
                "email": "test@gmail.com",
                "password": "test12345",
                "password2": "test",
            },
        )
        assert response.status_code == 400
        assert response.data == {"password": "Password must match."}
