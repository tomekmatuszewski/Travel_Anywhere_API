from typing import Union

from django.contrib.auth.models import User


def validate_email(email: str) -> Union[str, None]:
    try:
        user = User.objects.get(email=email.lower())
    except User.DoesNotExist:
        return None
    return email


def validate_username(username: str) -> Union[str, None]:
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return None
    return username


def error_message(email=None, username=None) -> dict:
    wrong_data = None
    if email:
        wrong_data = "email"
    elif username:
        wrong_data = "username"
    data = {
        "error message": f"That {wrong_data} is already in use",
        "response": "Error",
    }
    return data


def email_lowercase(data: dict) -> dict:
    email = data["email"]
    data.update({"email": email.lower()})
    return data


def check_matching_passwords(data: dict):
    new_password = data.get("new_password")
    confirm_new_password = data.get("confirm_new_password")
    if new_password != confirm_new_password:
        return None
    else:
        return data
