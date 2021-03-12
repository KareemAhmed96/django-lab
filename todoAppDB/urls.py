from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.addTask, name="addTask"),
    path('delete/<int:id>', views.deleteTask, name="deleteTask"),
]