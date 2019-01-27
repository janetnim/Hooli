from django.urls import path
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import UserView, LoginView


app_name = 'authentication'

router = DefaultRouter()
router.register('authentication', UserView, base_name='authentication')
router.register('authentication', LoginView, base_name='authentication')

urlpatterns = [
    path('user/', UserView.as_view()),
    path('user/login/', LoginView.as_view()),
]
