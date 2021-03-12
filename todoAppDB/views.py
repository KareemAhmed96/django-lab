from django.shortcuts import render, redirect


tasks = ["task1", "task2", "task3"]

# Create your views here.
def index(request):
    return render(request, "todoAppDB/index.html", {
        "tasks": tasks
    })