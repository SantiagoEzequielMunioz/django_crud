
from django.urls import path
from .views import ListPatients

urlpatterns = [
    path('', ListPatients.as_view(), name='index')
]