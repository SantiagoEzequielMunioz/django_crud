from django.shortcuts import render
from django.views.generic import ListView
from .models import Patient

# a list of patients
class ListPatients(ListView):
    model = Patient
    template_name = 'index.html'
