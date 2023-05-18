from rest_framework import serializers
from .models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        # fields = ['id', 'user', 'title'] # список полей для сериализации
        fields = '__all__'
        # exclude = ['updated_at'] # список полей для исключения


class ToDoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        exclude = ['id']
        read_only_fields = ['created_at', 'updated_at']


class ToDoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
    