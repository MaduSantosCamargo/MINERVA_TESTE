from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from .models import Todos
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from datetime import datetime

class TodosListView(ListView):
    model = Todos

class TodosCreateView(CreateView):
    model = Todos
    fields = ["titulo", "data_entrega"]
    success_url = reverse_lazy("todos_list")

class TodosUpdateViews(UpdateView):
    model = Todos
    fields =["titulo", "data_entrega"]
    success_url = reverse_lazy("todos_list")

class TodosDeleteView(DeleteView):
    model = Todos
    success_url = reverse_lazy("todos_list")

class TodosCompleteView(View):
    def get(self, request, pk):
        todos = get_object_or_404(Todos, pk=pk)
        todos.mark_has_complete()
        return redirect("todos_list")
        
