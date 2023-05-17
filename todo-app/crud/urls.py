from django.urls import path

from .views import ToDoListView


urlpatterns = [
    path('todos/', ToDoListView.as_view()),
    
]