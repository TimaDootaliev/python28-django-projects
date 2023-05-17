from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import ToDo
from .serializers import ToDoSerializer


class ToDoListView(APIView):
    def get(self, request: Request):
        queryset = ToDo.objects.all()
        serializer = ToDoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ToDoCreateView(APIView):
    def post(self, request):
        ...

class ToDoUpdateView(APIView):
    ...


# TODO: дописать весь CRUD для ToDo
