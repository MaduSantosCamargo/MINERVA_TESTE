from django.shortcuts import render 
from django.views.generic import ListView
from .models import Todos

class TodosListView(ListView):
    model = Todos