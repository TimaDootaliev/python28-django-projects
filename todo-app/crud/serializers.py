from rest_framework import serializers
from .models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        # fields = ['id', 'user', 'title'] # список полей для сериализации
        fields = '__all__'
        # exclude = ['updated_at'] # список полей для исключения


obj = {
    'id': 1,
    'title': 'asdf',
    'status': 'done'
}

# PUT
{
    'id': 1,
    'title': 'new_title',
    'status': 'not completed'
}

# PATCH
{
    'title': 'new_title'
}
