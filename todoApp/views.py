from django.shortcuts import render, redirect


# Create your views here.
tasks = []


def index(request):
    if request.method == "POST":
        task = request.POST['task']
        tasks.append(task)
        return redirect("index")

    return render(request, "todoApp/index.html", {
        "tasks": tasks
    })


def delete(request):
    if request.POST.get('DeleteButton'):
        print("DELETE")
        task = request.POST['DeleteButton']
        tasks.remove(task)
        return redirect("index")

    return render(request, "todoApp/index.html", {
        "tasks": tasks
    })
