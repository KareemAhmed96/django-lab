from django.shortcuts import render, redirect
from todoAppDB.models import Task


# Create your views here.
def index(request):
    tasks = Task.objects.all()

    return render(request, "todoAppDB/index.html", {
        "tasks": tasks
    })


def addTask(request):
    if request.method == "POST":
        name = request.POST.get("taskName")
        desc = request.POST.get("taskDescription")
        priority = request.POST.get("taskPriority")
        state = 0

        task = Task.objects.create(
            name=name,
            desc=desc,
            state=state,
            priority=priority
        )

        return redirect("index")


def deleteTask(request, id):
    task = Task.objects.get(pk=id)
    print("*********", task)
    task.delete()

    return redirect("index")


def updateTask(request, id):
    task = Task.objects.get(pk=id)

    if request.method == "POST":
        name = request.POST.get("name")
        desc = request.POST.get("desc")
        priority = request.POST.get("priority")

        task.name = name
        task.desc = desc
        task.priority = priority

        task.save()

        return redirect("index")


def doneTask(request, id):
    task = Task.objects.get(pk=id)

    task.state = 1

    task.save()

    return redirect("index")