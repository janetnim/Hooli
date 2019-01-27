from django.db import models
import jwt
from datetime import datetime, timedelta
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

class UserManager(BaseUserManager): # inherits from the BaseUserManager class
  def create_user(self, username, email, password):
    user = self.model(username = username, email=email)
    user.set_password(password)
    user.save()
    return user

  def create_superuser(self, username, email, password):
    user = self.create_user(self, username, email, password)
    user_is_superuser(True)
    user_is_active(True)
    user_is_admin(True)
    user_is_staff(True)
    user.save()


class User(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(max_length=100, unique=True, db_index=True)
  email = models.EmailField(db_index=True, unique=True)
  location = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  updated_at = models.DateTimeField(auto_now=True)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  is_staff = models.BaseUserManager(default=False)
  is_driver = models.BooleanField(default=False)

  USERNAME_FIELD = 'email' # this is the field we want to log in with
  REQUIRED_FIELD = ['username']

  objects = UserManager() #tells the model to save objects as described in the userManager class

  def __str__(self):
    #lets us convert user details to string and display it in case we are printing on the console
    return self.email

  def token(self):
    # will add the token implementation here
    return self._generate_jwt_token()

  def _generate_jwt_token(self):
    #will put jwt implementation here
    return None
    # expiry_date = datetime.now() + timedelta(days=30)
    # token = jwt.encode({
    #   'id': self.id,
    #   'exp': int(expiry_date.strftime('%s'))
    # }, 'ThisIstheSecretKey', algorithm='HS256')
    # return token.encode('utf-8')
