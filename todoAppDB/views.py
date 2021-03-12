from django.shortcuts import render, redirect
from todoAppDB.models import Task

tasks = Task.objects.all()


# Create your views here.
def index(request):
    return render(request, "todoAppDB/index.html", {
        "tasks": tasks
    })

