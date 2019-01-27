from rest_framework.views import APIView
from .models import User
from rest_framework import status
from .serializer import UserSerializer, LoginSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .renderers import UserJSONRenderer


class UserView(APIView):

  permission_classes = (AllowAny, )
  renderer_classes = (UserJSONRenderer,)
  serializer_class = UserSerializer

  def post(self, request):
    user = request.data.get('user', {})
    serializer = self.serializer_class(data=user)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)

class LoginView(APIView):

  permission_classes = (AllowAny, )
  renderer_classes = (UserJSONRenderer,)
  serializer_class = LoginSerializer

  def post(self, request):
    user = request.data.get('user', {})
    serializer = self.serializer_class(data=user)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
