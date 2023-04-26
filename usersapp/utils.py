from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework import serializers


def get_and_authenticate_user(email, password):
    user = authenticate(email=email, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid username/password. Please try again!")
    return user


def create_user_account(email, password, first_name="", last_name="", **extra_fields):
    user = get_user_model().objects.create_user(
        username=email,
        email=email,
        password=password, 
        first_name=first_name,
        last_name=last_name, 
        **extra_fields)

    return user