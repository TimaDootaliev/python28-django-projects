from django.urls import path
from .views import RegistrationView, ActivationView


urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('activate/', ActivationView.as_view(), name='activate')
]
