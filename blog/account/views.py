from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer, ActivationSerializer


class RegistrationView(CreateAPIView):
    serializer_class = RegistrationSerializer


class ActivationView(CreateAPIView):
    serializer_class = ActivationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.activate()
        return Response(
            {'message': 'Аккаунт успешно активирован'},
            status=status.HTTP_202_ACCEPTED
            )


