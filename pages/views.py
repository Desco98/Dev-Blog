from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Posts
from django.core.paginator import Paginator

def index(request):
    post_list = Posts.objects.order_by('-created_at').filter(is_published=True)

    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page')
    pages = paginator.get_page(page_number)
    
    context = {
        'posts': post_list,
        'pages': pages
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
