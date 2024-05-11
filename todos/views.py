from django.views.generic import ListView, CreateView
from .models import Todos
from django.urls import reverse_lazy

class TodosListView(ListView):
    model = Todos

class TodosCreateView(CreateView):
    model = Todos
    fields = ["titulo", "data_entrega"]
    success_url = reverse_lazy("todos_list")