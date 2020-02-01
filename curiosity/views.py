from django.shortcuts import render
from .models import Post


def wall(request):
    return render(request, 'wall.html', {
        "posts": Post.objects.order_by('-pub_date')
    })


def post(request, pk):

    return render(request, 'post.html', {
        "post": Post.objects.get(pk=pk)
    })
