from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
import json


def wall(request):
    return render(request, 'wall.html', {
        "posts": Post.objects.order_by('-pub_date')
    })


def post(request, pk):
    return render(request, 'post.html', {
        "post": Post.objects.get(pk=pk)
    })


@login_required(login_url="auth/login")
def write(request):
    if request.method == "POST":
        content = json.loads(request.body)
        if "pk" in content:
            Post.objects.filter(pk=content["pk"]).update(
                question=content["question"],
                answer=content["answer"]
            )
        else:
            Post.objects.create(
                question=content["question"],
                answer=content["answer"]
            )
        return redirect("/")
    elif "pk" in request.GET:
        pk = request.GET["pk"]
        return render(request, 'write.html', {"post": Post.objects.get(pk=pk)})
    else:
        return render(request, 'write.html')


@login_required(login_url="auth/login")
def manage(request):
    if request.method == "POST":
        content = json.loads(request.body)
        operation = content["operation"]
        pk = content["pk"]
        if operation == "edit":
            return redirect("/write?pk="+str(pk))
        elif operation == "delete":
            Post.objects.get(pk=pk).delete()
            return redirect("/manage")
    else:
        return render(request, 'manage.html', {
            "posts": Post.objects.order_by('-pub_date')
        })
