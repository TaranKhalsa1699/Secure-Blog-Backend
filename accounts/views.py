from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import generics
from .serializers import RegisterSerializer  # make sure this exists

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class LoginView(TokenObtainPairView):
    pass

class RefreshTokenView(TokenRefreshView):
    pass
