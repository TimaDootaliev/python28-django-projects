from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from .serializers import RegistrationSerializer, ActivationSerializer, LoginSerializer


class RegistrationView(CreateAPIView):
    serializer_class = RegistrationSerializer


class ActivationView(CreateAPIView):
    serializer_class = ActivationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.activate()
        return Response(
            {"message": "Аккаунт успешно активирован"}, status=status.HTTP_202_ACCEPTED
        )


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutView(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        print(request.user.username)
        Token.objects.get(user=request.user).delete()
        return Response({"message": "Logged Out"}, status=status.HTTP_204_NO_CONTENT)
