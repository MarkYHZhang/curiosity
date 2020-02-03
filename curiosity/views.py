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
        from datetime import datetime
        from pytz import timezone
        tz = timezone('EST')
        Post.objects.create(question=content["question"], answer=content["answer"], pub_date=datetime.now(tz))
        print(datetime.now(tz))
        return redirect("/")
    else:
        return render(request, 'write.html')


@login_required(login_url="auth/login")
def manage(request):
    if request.method == "POST":
        content = json.loads(request.body)
        from datetime import datetime
        from pytz import timezone
        tz = timezone('EST')
        Post.objects.create(question=content["question"], answer=content["answer"], pub_date=datetime.now(tz))
        print(datetime.now(tz))
        return redirect("/")
    else:
        return render(request, 'write.html')