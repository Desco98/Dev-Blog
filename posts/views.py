from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Posts

def lpost(request):
    latest_post = Posts.objects.latest('created_at')
    
    return render(request, 'posts/latest_post.html', { 'lpost': latest_post })

def post(request, post_id):
    posts = get_object_or_404(Posts, pk=post_id)
    return render(request, 'posts/post.html', { 'post': posts})