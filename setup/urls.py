from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path

from todos.views import TodosListView
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodosListView.as_view()),   
]
