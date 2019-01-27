# The serializer converts complex datatypes into json, xml etc simpler
# datatypes

from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User
import re

class UserSerializer(serializers.Serializer):
  email = serializers.CharField(max_length=255)
  username = serializers.CharField(max_length=255)
  password = serializers.CharField(max_length=128, min_length=8)
  token = serializers.CharField(read_only=True)

  class Meta:
    model = User
    fields = ['username', 'email', 'password', 'token']

  # def existing_user(self, key):
  #   find_user = User.objects.get(key=key)
  #   if find_user:
  #     raise serializers.ValidationError(
  #         'A user with this username already exists'
  #     )

  def validate(self, data):
    password = data.get('password', None)
    username = data.get('username', None)
    email = data.get('email', None)

    # new_username = User.objects.get(username=username)
    # print(new_username, '>>>>>>>>>>>>>')
    # if not new_username:
    #   raise serializers.ValidationError(
    #       'A user with this username already exists'
    #   )

    # new_email = User.objects.get(email=email)
    # print(new_email, '>>>>>>>>>>>>>>>>>>')
    # if new_email:
    #   raise serializers.ValidationError(
    #       'A user with this email already exists'
    #   )

    # Validate password has at least one small and capital letter
    if not re.match(r"^(?=.*[A-Z])(?=.*[a-z]).*", password):
            raise serializers.ValidationError(
                'A password must contain atleast one small letter and one capital letter.'
            )

    # Validate the password has atleast one number
    elif not re.match(r"^(?=.*[0-9]).*", password):
        raise serializers.ValidationError(
            'A password must contain atleast one number.'
        )
    return data

  def create(self, validate_data):
    return User.objects.create_user(**validate_data)


class LoginSerializer(serializers.Serializer):
  email = serializers.CharField(max_length=255)
  password = serializers.CharField(max_length=255)
  token = serializers.CharField(read_only=True)

  class Meta:
    model = User
    fields = ['email', 'password', 'token']

  def validate(self, data):
    email = data.get('email', None)
    password = data.get('password', None)
    user = authenticate(username=email, password=password)
    if not user:
      raise serializers.ValidationError(
          'A user with this email and password does not exist'
      )

    return data
