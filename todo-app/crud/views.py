from django.http import Http404
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import ToDo
from .serializers import ToDoSerializer, ToDoCreateSerializer, ToDoUpdateSerializer


class ToDoListView(APIView):
    def get(self, request: Request):
        queryset = ToDo.objects.all()
        serializer = ToDoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ToDoCreateView(APIView):
    def post(self, request: Request):
        serializer = ToDoCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ToDoUpdateView(APIView):
    def patch(self, request: Request, pk):
        try:
            todo = ToDo.objects.get(pk=pk) # -> ToDo object
        except ToDo.DoesNotExist:
            raise Http404
        serializer = ToDoUpdateSerializer(instance=todo, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class ToDoDeleteView(APIView):
    def delete(self, request: Request, pk):
        try:
            todo = ToDo.objects.get(pk=pk)
        except ToDo.DoesNotExist:
            raise Http404
        todo.delete()
        return Response({'message': 'Deleted'}, status=status.HTTP_204_NO_CONTENT)


class ToDoDetailView(APIView):
    def get(self, request: Request, pk):
        try:
            todo = ToDo.objects.get(pk=pk)
        except ToDo.DoesNotExist:
            raise Http404
        serializer = ToDoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)




# TODO: дописать весь CRUD для ToDo
