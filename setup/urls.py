
from django.contrib import admin
from django.urls import path

from todos.views import TodosListView, TodosCreateView
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodosListView.as_view(), name="todos_list"),
    path("create", TodosCreateView.as_view(), name="todos_create"),
]
